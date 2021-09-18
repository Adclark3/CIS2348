# Avery Clark
# 1907691

print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')

service_dic = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12 }

print('Select first service:')
service1 = input()
print('Select second service:')
service2 = input('\n')

print("Davy's auto shop invoice\n")
if service1 == '-':
    service1_cost = 0
    print('Service 1: No service')
else:
    service1_cost = service_dic[service1]
    print('Service 1:', service1, end = '')
    print(', $', end='')
    print(service1_cost)
if service2 == '-':
    service2_cost = 0
    print('Service 2: No service')
else:
    service2_cost = service_dic[service2]
    print('Service 2:', service2, end='')
    print(', $', end='')
    print(service2_cost)

total = service1_cost + service2_cost
print('\nTotal: $', end='')
print(total)
