
scores_one=[]
scores_two=[]
print('Enter test scores for class 1.')
again = 'y'
while again == 'y':
    test_scores=float(input('Enter a test score:'))
    scores_one.append(test_scores)
    again = input('Do you want to enter another score? [y/n] \n')
    again = again.lower()
    print('\n')

print('Enter test scores for class 2.')
again = 'y'
while again=='y':
    scores=float(input('Enter a score:'))
    scores_two.append(scores)
    again = input('Do you want to enter another score? [y/n] \n')
    again = again.lower()
    print('\n')


num_scores_one=len(scores_one)
print('There are', num_scores_one,'students in class 1.')
print('Scores in class 0001:',scores_one,"\n")

num_scores_two=len(scores_two)
print('There are', num_scores_two,'students in class 2.')
print('Scores in class 0002:',scores_two,"\n")

total_scores=scores_two + scores_one
num_both_scores=len(total_scores)
print('There are', num_both_scores, 'students in class 1 and class 2 combined.')
print('Scores in combined list',total_scores,"\n")

highest=max(total_scores)
print('The highest score in the combined list is:',highest, '\n')
lowest=min(total_scores)
print('The lowest score in the combined list is:',lowest, '\n')

total_scores.sort()
print('Scores in the combined list sorted in ascending order:', total_scores,"\n")

total_scores.reverse()
print('Scores in the combined list sorted in descending order:',total_scores,"\n")
