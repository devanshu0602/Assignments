def First_in_first_out(frame_size, page_references):
    frame = []
    page_hits = 0
    page_faults = 0
    for page in page_references:
        if page in frame:
            print(f"Page HIT {page} => ", end="")
            page_hits = page_hits + 1
        else:
            print("Page FAULT => ", end="")
            page_faults = page_faults + 1
            if len(frame) < frame_size:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
        print("Frame =", frame)
    print("\nTotal Page Hits =", page_hits)
    print("Total Page Faults =", page_faults)
    hit_percentage = (page_hits * 100) / (page_hits + page_faults)
    print(f"Hit ratio = {hit_percentage}% | Miss ratio = {100 - hit_percentage}%")


def Least_recently_used(frame_size, page_references):
    frame = []
    page_hits = 0
    page_faults = 0
    for page in page_references:
        initial_frame = frame.copy()
        if page in frame:
            print(f"Page HIT {page} => ", end="")
            page_hits = page_hits + 1
            frame.remove(page)
            frame.append(page)
        else:
            print("Page FAULT => ", end="")
            page_faults = page_faults + 1
            if len(frame) < frame_size:
                frame.append(page)
            else:
                frame.remove(frame[0])
                frame.append(page)
        print("Frame =", frame)
    print("\nTotal Page Hits =", page_hits)
    print("Total Page Faults =", page_faults)
    hit_percentage = (page_hits * 100) / (page_hits + page_faults)
    print(f"Hit ratio = {hit_percentage}% | Miss ratio = {100 - hit_percentage}%")


def predict_page(page_references, frame, index):
    result = -1
    farthest_page = index
    for i in range(0, len(frame)):
        for j in range(index, len(page_references)):
            if frame[i] == page_references[j]:
                if j > farthest_page:
                    farthest_page = j
                    result = i
                break
    if result == -1:
        return 0
    else:
        return result
def Optimal(frame_size, page_references):
    frame = []
    page_hits = 0
    page_faults = 0
    for i in range(0, len(page_references)):
        if page_references[i] in frame:
            print(f"Page HIT {page_references[i]} => ", end="")
            page_hits = page_hits + 1
        else:
            print("Page FAULT => ", end="")
            page_faults = page_faults + 1
            if len(frame) < frame_size:
                frame.append(page_references[i])
            else:
                j = predict_page(page_references.copy(), frame.copy(), i + 1)
                frame[j] = page_references[i]
        print("Frame =", frame)
    print("\nTotal Page Hits =", page_hits)
    print("Total Page Faults =", page_faults)
    hit_percentage = (page_hits * 100) / (page_hits + page_faults)
    print(f"Hit ratio = {hit_percentage}% | Miss ratio = {100 - hit_percentage}%")


if __name__ == '__main__':
    # Header
    print("\nDevanshu Gupta [21BCE0597]\n")
    # Number of Page frames
    frame_size = int(input("Enter the number of Page Frames: "))
    # List of all page references
    page_references = input("Enter the page references: ")
    page_references = page_references.split(" ")
    page_references = [eval(i) for i in page_references]
    # Performing Page replacement
    print("\n--------------- Using F.I.F.O. ---------------")
    First_in_first_out(frame_size, page_references.copy())
    print("\n--------------- Using L.R.U. ---------------")
    Least_recently_used(frame_size, page_references.copy())
    print("\n--------------- Using OPTIMAL ---------------")
    Optimal(frame_size, page_references.copy())
    # Footer
    print("\nDevanshu Gupta [21BCE0597]\n")