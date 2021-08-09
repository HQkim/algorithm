# swea 1208 Flatten

for tc in range(1, 11):
    n = 100
    number_of_dump = int(input())
    boxes = list(map(int, input().split()))

    while number_of_dump > 0:
        number_of_dump -= 1

        max_height = max(boxes)
        min_height = min(boxes)

        max_ind = boxes.index(max_height)
        min_ind = boxes.index(min_height)

        boxes[max_ind] -= 1
        boxes[min_ind] += 1

    max_height = max(boxes)
    min_height = min(boxes)
    diff_height = max_height - min_height

    print(f'#{tc} {diff_height}')
