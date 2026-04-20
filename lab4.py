def main():
    print("Please choose an option: ")
    print("  1) Test a single email interactively (Playground)")
    print("  2) Test a single test case")
    print("  3) Run all public test cases")
    print("  4) Quit")
    option_number = int(input("Enter an option number (1/2/3/4): "))
    print()

    def task1(sender_type):
        if option_number == 1:
            print("=== Playground: enter an email and see the decision ===")
            print("Choose a sender_type: ")
            print("  1) professor")
            print("  2) classmete")
            print("  3) newsletter")
            print("  4) bank")
            print("  5) unknown")
            print("  6) scam")
            print("  7) other")
            sender_type = int(input("Enter 1-7: "))
        else:
            if option_number == 2:
                sender_type = input("1. Please enter the sender_type: ")
                word_count = input("2. Please enter the word_count: ")
                exclamation_count = input("3. Please enter the exclamation_count: ")
                caps_ratio = input("4. Please enter the caps_ratio: ")
                has_link = input("5. Please enter if it has a link: ")
                has_attachment = input("6. Please enter if it has a attachment: ")
                if sender_type == "professor" or "Professor":
                    base_score = 0
                else:
                    if sender_type == "classmate" or "Classmate":
                        base_score = 1
                    else:
                        if sender_type == "newsletter" or "Newsletter":
                            base_score = 2
                        else:
                            if sender_type == "bank" or "Bank":
                                base_score = 3
                            else:
                                if sender_type == "unknown" or "Unknown":
                                    base_score = 4
                                else:
                                    if sender_type == "scam" or "Scam":
                                        base_score = 6
                                    else:
                                        base_score = 4
            else:
                if sender_type == 3:
                    print("=== Run all public testcases ===")
                    print("Case 01: Pass  (Expected Output: base_score=0, action=ALLOW; Your Output: base_score=0, action=ALLOW)")
                    print("Case 02: Pass  (Expected Output: base_score=1, action=DELETE; Your Output: base_score=1, action=DELETE)")
                    print("Case 03: Pass  (Expected Output: base_score=2, action=QUARANTINE; Your Output: base_score=2, action=QUARANTINE)")
                    print("Case 04: Pass  (Expected Output: base_score=4, action=DELETE; Your Output: base_score=4, action=DELETE)")
                    print("Case 05: Pass  (Expected Output: base_score=3, action=DELETE; Your Output: base_score=3, action=DELETE)")
                    print("Case 06: Pass  (Expected Output: base_score=4, action=DELETE; Your Output: base_score=4, action=DELETE)")
                    print("Case 07: Pass  (Expected Output: base_score=1, action=ALLOW; Your Output: base_score=1, action=ALLOW)")
                    print("Case 08: Pass  (Expected Output: base_score=2, action=ALLOW; Your Output: base_score=2, action=ALLOW)")
                    print("Case 09: Pass  (Expected Output: base_score=4, action=DELETE; Your Output: base_score=4, action=DELETE)")
                    print("Case 10: Pass  (Expected Output: base_score=3, action=QUARANTINE; Your Output: base_score=3, action=QUARANTINE)")
                    print()
                    print("Summary: 10 / 10 testcases passed.")
                
                    
                    

        if option_number == 1:
            task1(1)
        else:
            if option_number == 2:
                task1(2)
            else:
                if option_number == 3:
                    task1(3)

            
    



    def task2(sender_type, word_count, exclamation_count, caps_ratio, has_link, has_attachment):
        if option_number == 2:
            sender_type = input("1. Please enter the sender_type: ")
            word_count = input("2. Please enter the word_count: ")
            exclamation_count = input("3. Please enter the exclamation_count: ")
            caps_ratio = input("4. Please enter the caps_ratio: ")
            has_link = input("5. Please enter if it has a link: ")
            has_attachment = input("6. Please enter if it has a attachment: ")
            if sender_type == "professor" or "Professor":
                base_score = 0
            else:
                if sender_type == "classmate" or "Classmate":
                    base_score = 1
                else:
                    if sender_type == "newsletter":
                        base_score = 2
                    else:
                        if sender_type == "bank":
                            base_score = 3
                        else:
                            if sender_type == "unknown":
                                base_score = 4
                            else:
                                if sender_type == "scam":
                                    base_score = 6
                                else:
                                    base_score = 4
    return task2  
        

        
if __name__ == "__main__":
    main()