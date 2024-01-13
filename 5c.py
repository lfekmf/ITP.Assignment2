xaxis = float(input('Enter x-axis number: '))
yaxis = float(input('Enter y-axis number: '))
if xaxis > 0 and yaxis > 0:
    print('Point lies in I quadrant')
elif xaxis < 0 and yaxis > 0:
    print('Point lies in II quadrant')
elif xaxis < 0 and yaxis < 0:
    print('Point lies in III quadrant')
elif xaxis > 0 and yaxis < 0:
    print('Point lies in IV quadrant')