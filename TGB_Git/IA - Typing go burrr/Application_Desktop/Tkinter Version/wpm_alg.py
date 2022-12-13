# calculate words per minute and accuracy
def calculate_wpm_and_accuracy(time_taken, num_words):
  # calculate words per minute
  wpm = num_words / (time_taken / 60)
  
  # calculate accuracy
  accuracy = num_words / (time_taken / 60)
  
  # return the results
  return wpm, accuracy

# time taken to type a passage of text (in seconds)
time_taken = 15

# number of words typed in the passage
num_words = 20

# calculate words per minute and accuracy
wpm, acc = calculate_wpm_and_accuracy(time_taken, num_words)

# print the results
print("Words per minute:", wpm)
print("Accuracy:", acc)
