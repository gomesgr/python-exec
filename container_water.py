# Dada uma lista de alturas
# Encontre um container com a maior area que possa ser
# preenchida por agua

def container_with_most_water(heights):
    max_area = 0
    left, right = 0, len(heights) - 1
    while left < right:
        area = min(heights[left], heights[right]) * (right - left)
        max_area = max(max_area, area)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area

l = [1, 3, 2, 0, 5, 2, 5, 4, 1, 2]

print(container_with_most_water(l))
