# Noktaların tanımlanması
points = [(2,3),(5,6),(8,9),(10,11),(12,13)]

# Öklid mesafesi için bir fonksiyon yazma
def euclideanDistance(point1,point2):
    x1,y1 = point1
    x2,y2 = point2 
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i+1,len(points)):
        distance = euclideanDistance(points[i],points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)

# Sonucun yazdırılması
print("Minimum mesafe:",min_distance)