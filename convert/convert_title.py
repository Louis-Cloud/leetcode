"""
Takes in Leetcode title and returns id for problem

Parameters
----------
title: title of leetcode problem
"""
def get_id(title):
    return title.lower().replace(' ', '-')

def main():
    # Prompts user for Leetcode title
    title = input("Enter title: ")
    # Prints out Leetcode url
    print(f"https://leetcode.com/problems/{get_id(title)}")

if __name__ == "__main__":
    main()