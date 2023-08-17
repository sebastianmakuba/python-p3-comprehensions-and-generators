#!/usr/bin/env python3

def return_evens(num_list):
    evens = [x for x in num_list if x % 2 ==0]
    return(evens)
    [x for x in num_list if x % 2 != 0]
    return []
    pass
return_evens([0, 1, 3, 5, 7, 8, 9])
def make_exclamation(sentence_list):
  exclamation_list = [sentence + "!" for sentence in sentence_list]
  return exclamation_list
  sentence_list = [x for x in sentence_list if sentence_list == []]
  return []
   
make_exclamation(["I like computers",
            "I require coffee",
            "Live long and prosper",])