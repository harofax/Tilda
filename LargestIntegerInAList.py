# Find the largest integer between (-10000, 10000)
# in a randomly large list that is the smallest missing consecutive non negative integer
# Example [-4000, -2, -1, 1,2,3,4,5,6,7,1000]: answer: 8
# Example [-1, -1, -1, -1]: answer: 1
from random import randint


def makeInputData():
    return [randint(-10, 10) for _ in range(50)]


def findLargestPositiveInteger(inputData):
    candidate = 1
    current_smallest = 1

    for i in range(len(inputData)):
        next_element = inputData[i]
        if next_element <= 0:
            continue
        else:
            if candidate == next_element:
                candidate = next_element + 1
                continue
            if next_element < current_smallest:
                current_smallest = next_element
                if next_element + 1 == candidate:
                    candidate = current_smallest + 1

            # if current_smallest == candidate + 1:
            #     candidate = current_smallest
            #     continue


    return candidate


def main():
    inputData = makeInputData()
    largestInteger = findLargestPositiveInteger(inputData)  # [-1,-1,-1,-1,47,48,49,1])

    #inputData = [-10, -10, -10, -10, -10, -9, -9, -9, -9, -9, -9, -8, -8, -8, -7, -6, -5, -5, -5, -5, -5, -4, -4, -4,
    #             -3, -3, -2, -1, 0, 1, 1, 1, 2, 2, 2, 2, 4, 4, 5, 6, 6, 6, 6, 7, 8, 8, 8, 9, 9, 10]

    inputData.sort()
    print(inputData, "\n")
    print("Answer: ", largestInteger)


if __name__ == "__main__":
    main()
