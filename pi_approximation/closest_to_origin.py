class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclid_dict = {}
        
        for v in range(len(points)):
            euclid_dist = math.sqrt((points[v][0]**2) + (points[v][1]**2))
            if euclid_dist not in euclid_dict:
                euclid_dict[euclid_dist] = []
            euclid_dict[euclid_dist].append(tuple(points[v]))
        
        result = []
        for dist in sorted(euclid_dict.keys()):
            result.extend(euclid_dict[dist])
            if len(result) >= k:
                break
                
        return result[:k]