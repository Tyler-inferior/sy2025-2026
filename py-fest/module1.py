F1 = {"f1", "w off road-bug", 185, (104, 142), 6000, 9, 1600, 4}
C4 = {"c4", "Citroen Saxo Kit-Car", 168, (161, 220), 6000, 7.5, 1600, 4}
A2 = {"a2", "Ford Focus WRC", 224, (221,300), 5400, 5.5, 1995, 4}
A1 = {"a1", "Hyundai Accent WRC", 220, (221,300), 5500, 5.4, 1998, 4}
B4 = {"b4", "VW Golf Kit-Car", 220, (191, 260), 8000, 6.2, 1998, 4}
F4 = {"f4", "PRD Racing Team", 200, (125, 170), 6500, 7.1, 2700, 4}
D1 = {"d1", "Mitsubishi Lancer RS", 220, (219, 290), 6200, 5.9, 1997, 4}
H2 = {"h2", "Mitsubishi Lancer", 198, (213, 290), 5500, 7.2, 1997, 4}
E4 = {"e4", "Austin Metro 6", 240, (265, 360), 9800, 3.4, 3600, 6}
B2 = {"b2", "Opel Kadett 4x4", 225, (221, 300), 8600, 6.5, 1980, 4}

cars = {F1, C4, A2, A1, B4, F4, D1, H2, E4, B2}
i =1
for car in cars:
    print(i,car[1])
    i +=1
