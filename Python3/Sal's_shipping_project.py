def ground_shipping(weight):
    if weight <= 2:
      cost = weight * 1.50 + 20.00
      return cost
    if weight > 2 and weight <= 6:
      cost = weight * 3.00 + 20.00
      return cost
    if weight > 6 and weight <= 10 :
      cost = weight * 4.00 + 20.00
      return cost
    if weight > 10:
      cost = weight * 4.75 + 20.00
      return cost

premium_ground = 125.00

def drone_shipping(weight):
    if weight <= 2:
      cost = weight * 4.50 
      return cost
    if weight > 2 and weight <= 6:
      cost = weight * 9.00
      return cost
    if weight > 6 and weight <= 10 :
      cost = weight * 12.00
      return cost
    if weight > 10:
      cost = weight * 14.25
      return cost
 
def cheapest_shipping_method(weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < 125:
    return "You should ship using ground shipping, it will cost " + "$" + str(ground_shipping(weight))
  if drone_shipping(weight) < ground_shipping(weight) < 125:
    return "You should ship using drone shipping, it will cost " + "$" + str(drone_shipping(weight))
  else:
    return "You should ship using premium ground shipping, it will cost " + "$" + str(premium_ground)
  
print(cheapest_shipping_method(4.8))   

print(cheapest_shipping_method(41.5))
    
    
    
    
    
    