aliens = []
for _ in range(1,10):
    new_alien = {'color': 'green', 'speed': 'slow', 'point': 5}
    aliens.append(new_alien)
for alien in aliens[:3]:
    print(alien)
print("....")
print(f"Total number of aliens : {len(aliens)}")

# изменяем данные последних трех
for alien in aliens[3:]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
for alien in aliens[6:]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['point'] = 15
for alien in aliens:
    print(alien)
