# Real-World Performance Case Studies

This document contains examples of actual performance issues and their solutions from real-world scenarios.

---

## Case Study 1: E-commerce Product Search

### Problem
An e-commerce website's product search was taking 3-5 seconds for queries, resulting in poor user experience and high bounce rates.

### Root Cause
```python
# Inefficient implementation
def search_products(query, all_products):
    results = []
    for product in all_products:  # 100,000+ products
        if query.lower() in product.name.lower() or \
           query.lower() in product.description.lower():
            results.append(product)
    return results
```

**Issues:**
- O(n) linear search through all products
- String operations on every product for every search
- No caching of search results
- Database queries inside the loop (not shown)

### Solution
```python
# Optimized implementation using search index
from whoosh import index
from whoosh.qparser import QueryParser

class ProductSearchIndex:
    def __init__(self):
        self.ix = create_index()
        
    def search(self, query):
        with self.ix.searcher() as searcher:
            parser = QueryParser("content", self.ix.schema)
            q = parser.parse(query)
            results = searcher.search(q, limit=50)
            return [r['product_id'] for r in results]

# With caching
from functools import lru_cache

@lru_cache(maxsize=1000)
def search_products_cached(query):
    return product_index.search(query)
```

**Improvements:**
- Search time reduced from 3-5s to 50-100ms (30-50x faster)
- Used dedicated search index (Elasticsearch/Whoosh)
- Added LRU cache for common queries
- Pre-computed search metadata during indexing

**Impact:**
- Bounce rate decreased by 40%
- Conversion rate increased by 15%
- Server load reduced by 60%

---

## Case Study 2: Analytics Dashboard Data Aggregation

### Problem
A dashboard showing user analytics was timing out after 30 seconds when loading data for large organizations.

### Root Cause
```python
# Inefficient implementation
def get_user_statistics(org_id):
    users = User.objects.filter(organization=org_id)
    stats = []
    for user in users:  # N+1 query problem
        login_count = Login.objects.filter(user=user).count()
        page_views = PageView.objects.filter(user=user).count()
        last_activity = Activity.objects.filter(user=user).order_by('-created_at').first()
        stats.append({
            'user': user,
            'logins': login_count,
            'views': page_views,
            'last_seen': last_activity.created_at if last_activity else None
        })
    return stats
```

**Issues:**
- N+1 query problem (1 + 3N queries for N users)
- No database indexes on foreign keys
- Computing statistics on every request
- No pagination

### Solution
```python
# Optimized implementation
from django.db.models import Count, Max, Prefetch

def get_user_statistics(org_id, page=1, per_page=50):
    # Single query with aggregations
    users = User.objects.filter(
        organization=org_id
    ).annotate(
        login_count=Count('login'),
        page_view_count=Count('pageview'),
        last_activity=Max('activity__created_at')
    ).select_related('organization')[
        (page-1)*per_page : page*per_page
    ]
    
    return [
        {
            'user': user,
            'logins': user.login_count,
            'views': user.page_view_count,
            'last_seen': user.last_activity
        }
        for user in users
    ]

# Background job for pre-computation
def update_user_stats_cache():
    """Run periodically to cache statistics"""
    for org in Organization.objects.all():
        stats = compute_stats(org.id)
        cache.set(f'org_stats_{org.id}', stats, timeout=3600)
```

**Improvements:**
- Reduced queries from 1+3N to 1
- Added database indexes
- Implemented pagination
- Pre-computed statistics in background jobs
- Added Redis caching layer

**Results:**
- Page load time: 30s → 200ms (150x faster)
- Database load reduced by 95%
- Can handle 10x more concurrent users

---

## Case Study 3: Image Processing Service

### Problem
An image resizing service was processing only 10 images per second, causing a backlog of thousands of images.

### Root Cause
```python
# Inefficient implementation
def process_images(image_list):
    results = []
    for image_path in image_list:
        # Sequential processing
        img = Image.open(image_path)
        
        # Multiple resize operations
        thumbnail = img.resize((100, 100))
        thumbnail.save(f'{image_path}_thumb.jpg')
        
        medium = img.resize((500, 500))
        medium.save(f'{image_path}_medium.jpg')
        
        large = img.resize((1200, 1200))
        large.save(f'{image_path}_large.jpg')
        
        results.append(image_path)
    return results
```

**Issues:**
- Sequential processing (single-threaded)
- Loading full image multiple times
- No optimization of I/O operations
- Missing error handling

### Solution
```python
# Optimized implementation
from multiprocessing import Pool
from PIL import Image
import os

def process_single_image(args):
    """Process one image with all size variants"""
    image_path, sizes = args
    try:
        with Image.open(image_path) as img:
            # Convert to RGB if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            results = []
            for name, size in sizes.items():
                # Use thumbnail() for better performance
                img_copy = img.copy()
                img_copy.thumbnail(size, Image.LANCZOS)
                
                output_path = f'{image_path}_{name}.jpg'
                img_copy.save(output_path, 'JPEG', quality=85, optimize=True)
                results.append(output_path)
            
            return {'success': True, 'files': results}
    except Exception as e:
        return {'success': False, 'error': str(e), 'file': image_path}

def process_images_parallel(image_list):
    """Process images in parallel"""
    sizes = {
        'thumb': (100, 100),
        'medium': (500, 500),
        'large': (1200, 1200)
    }
    
    # Use all available CPU cores
    with Pool() as pool:
        args = [(img_path, sizes) for img_path in image_list]
        results = pool.map(process_single_image, args)
    
    return results
```

**Improvements:**
- Used multiprocessing to utilize all CPU cores
- Optimized image operations (thumbnail() vs resize())
- Reduced I/O by opening image once
- Added JPEG optimization
- Proper error handling

**Results:**
- Processing speed: 10 images/s → 200 images/s (20x faster)
- Cleared backlog in 2 hours instead of 40 hours
- Reduced server costs by 70%

---

## Case Study 4: API Response Time

### Problem
A REST API endpoint was consistently slow (2-4 seconds response time) causing mobile app timeouts.

### Root Cause
```python
# Inefficient implementation
@app.route('/api/feed')
def get_user_feed():
    user_id = request.args.get('user_id')
    
    # Fetch user
    user = db.query(f"SELECT * FROM users WHERE id = {user_id}").first()
    
    # Fetch all posts from friends (not paginated)
    friend_ids = [f.id for f in user.friends]
    posts = []
    for friend_id in friend_ids:
        friend_posts = db.query(
            f"SELECT * FROM posts WHERE user_id = {friend_id}"
        ).all()
        posts.extend(friend_posts)
    
    # Sort by date
    posts.sort(key=lambda x: x.created_at, reverse=True)
    
    # Fetch likes and comments for each post
    for post in posts:
        post.likes = db.query(f"SELECT * FROM likes WHERE post_id = {post.id}").all()
        post.comments = db.query(f"SELECT * FROM comments WHERE post_id = {post.id}").all()
    
    return jsonify({'posts': posts[:20]})  # Only return 20 anyway!
```

**Issues:**
- N+1 queries for friends' posts
- Fetching all posts then discarding most
- No pagination at database level
- No caching
- SQL injection vulnerability (bonus issue!)
- Nested N+1 for likes and comments

### Solution
```python
# Optimized implementation
from flask_caching import Cache
from sqlalchemy import desc

cache = Cache(config={'CACHE_TYPE': 'redis'})

@app.route('/api/feed')
@cache.cached(timeout=60, query_string=True)
def get_user_feed():
    user_id = request.args.get('user_id', type=int)
    page = request.args.get('page', 1, type=int)
    per_page = 20
    
    # Single optimized query with proper joins
    posts = db.session.query(Post)\
        .join(User, Post.user_id == User.id)\
        .join(Friendship, Friendship.friend_id == User.id)\
        .filter(Friendship.user_id == user_id)\
        .options(
            joinedload(Post.user),
            selectinload(Post.likes),
            selectinload(Post.comments)
        )\
        .order_by(desc(Post.created_at))\
        .limit(per_page)\
        .offset((page - 1) * per_page)\
        .all()
    
    return jsonify({
        'posts': [post.to_dict() for post in posts],
        'page': page,
        'has_more': len(posts) == per_page
    })
```

**Improvements:**
- Reduced to single query with joins
- Proper use of ORM eager loading
- Added Redis caching (60s TTL)
- Pagination at database level
- Fixed SQL injection vulnerability
- Added database indexes

**Results:**
- Response time: 2-4s → 50-100ms (20-40x faster)
- Mobile app timeout issues resolved
- API can handle 10x more requests
- Database CPU usage dropped 80%

---

## Key Lessons Learned

### 1. Always Profile First
Don't assume you know where the bottleneck is. Use profiling tools to find the actual problem.

### 2. Database Optimization
- Avoid N+1 queries
- Add indexes strategically
- Use pagination
- Implement caching

### 3. Parallel Processing
For independent tasks (image processing, API calls), use parallel execution.

### 4. Caching Strategy
- Cache expensive operations
- Set appropriate TTLs
- Invalidate cache when data changes
- Use tiered caching (memory → Redis → database)

### 5. Choose the Right Tool
- Use specialized solutions (search indexes, message queues)
- Don't reinvent optimized solutions
- Consider managed services for complex operations

### 6. Monitor and Iterate
- Set up performance monitoring
- Track key metrics over time
- Continuously optimize hot paths
- A/B test optimizations in production

---

## Optimization Checklist

Before optimizing any system:

- [ ] Set up performance monitoring
- [ ] Profile to identify bottlenecks
- [ ] Measure current performance metrics
- [ ] Review database queries and indexes
- [ ] Check for N+1 query patterns
- [ ] Evaluate caching opportunities
- [ ] Consider async/parallel processing
- [ ] Review algorithm complexity
- [ ] Test with production-like data
- [ ] Measure improvement after changes
- [ ] Monitor for regressions

Remember: Optimization is a continuous process, not a one-time fix!
