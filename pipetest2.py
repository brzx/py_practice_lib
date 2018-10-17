def even_filter(nums):
    return filter(lambda x: x%2==0, nums)
 
def multiply_by_three(nums):
    return map(lambda x: x*3, nums)
 
def convert_to_string(nums):
    return map(lambda x: 'The Number: %s' % x,  nums)

def pipeline_func(data, fns):
    return reduce(lambda a, x: x(a),
                  fns,
                  data)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pipeline = pipeline_func(nums, [even_filter,
                     multiply_by_three,
                     convert_to_string])

for num in pipeline:
    print num