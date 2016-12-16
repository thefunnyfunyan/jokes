import json

class Joke(object):
  def getJokeType(self):
    pass

  def tellJoke(self):
    pass

  def getRandomJoke(self):
    pass

class StoryJoke(Joke):
  def getJokeType(self):
    return 'Story Joke'
  
  def tellJoke(self):
    joke = self.getRandomJoke()
    print(joke)

  def getRandomJoke(self):
    return "Three men walk into a bar. The fourth one ducks"

class QuestionJoke(Joke):
  def getJokeType(self):
    return "Question Joke"

  def tellJoke(self):
    joke = self.getRandomJoke()
    print(joke[0])
    input()
    print(joke[1])

  def getRandomJoke(self):
    return ['Why did the little boy drop his ice cream cone?', 'Because he was hit by the school bus']

class KnockKnockJoke(object):
  def getJokeType(self):
    return 'Knock Knock Joke'

  def tellJoke(self):
    joke = self.getRandomJoke()
    print('Knock Knock')
    self.getProperInput('who there')
    print(joke[0])
    self.getProperInput(joke[0] + ' who')
    print(joke[1])

  def getProperInput(self, properInput):
    inputList = properInput.split(' ')
    while(True):
      userInput = input()
      for word in inputList:
        if word.upper() not in userInput.upper():
          print('Gotta play the game!')
          break
        return

  def getRandomJoke(self):
    return ['Boo', 'Awww its just a joke. There is no reason to cry about it.']


class JokeTeller(object):
  jokes = [StoryJoke(), QuestionJoke(), KnockKnockJoke()]

  def main(self):
    while True:
      for index, joke in enumerate(self.jokes):
        print(joke.getJokeType() + ': ' + str(index))
      
      jokeIndex = input("\nSelect a joke: ")
      self.jokes[int(jokeIndex)].tellJoke()
      repeat = input('more? (y)es/(n)o: ')
      if 'n' in repeat: return  

if __name__ == '__main__':
  jt = JokeTeller()
  jt.main()