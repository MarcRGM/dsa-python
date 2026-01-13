# Bucket sort means:

# Create buckets (containers)
# Distribute items into buckets based on some rule
# Sort inside each bucket (or rely on order)
# Collect buckets back in order

# When to use Bucket Sort

# Data has a known range
# Values are evenly distributed
# You want linear-ish time


# Sort numbers between 0 and 100.
nums = [29, 25, 3, 49, 9, 37, 21, 43]

# Step-by-step bucket sort

def bucket_sort(nums):
    if not nums:
        return nums

    # 1. Create buckets
    # 10 buckets: 0–9, 10–19, ..., 90–99
    buckets = [[] for _ in range(10)]

    # 2. Distribute numbers into buckets
    for n in nums:
        index = n // 10      # decide which bucket
        buckets[index].append(n)

    # 3. Sort each bucket
    for bucket in buckets:
        bucket.sort()

    # 4. Collect numbers back
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result

print(bucket_sort(nums))
