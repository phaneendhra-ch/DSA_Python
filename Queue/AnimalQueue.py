"""
Assignment Problem on Queues

Statement :
A queue contains animals of type : dog and cat

A person cannot select random animal of any type,he can select only the type and oldest dog will pop put

Author : Phaneendhra
"""

class Animals:

    def __init__(self):
        self.cats = []      #list for cats
        self.dogs = []      #list for dogs

    def enqueue(self,animal,type):
        if type == 'Cat':               #check if type is cat
            self.cats.append(animal)    #append to cat list, here the element at 0th index is our older animal
                                        #as new cat enters we are just appending it to the list
        else:
            self.dogs.append(animal)

    def dequeuecat(self):               #deque cat
        if len(self.cats) ==0:          #check if cats are available or not
            return None
        else:                           #if yes, then remove the first element,
            return self.cats.pop(0)     #as we are dequeing the cat which is older (or) the cat which we have inserted first into the list


    def dequeuedog(self):               #deque dog
        if len(self.dogs) ==0:          #check if dogs are available or not
            return None
        else:
            return self.dogs.pop(0)     #as we are dequeing the dog which is older (or) the dog which we have inserted first into the list

    def dequeueany(self):               #deque any
        """

        Here we will dequeue either the cat or dog depending upon the availability
        The dequeing happens, the animal which first inserted is been popped out.

        """
        if len(self.cats) == 0:
            return self.dogs.pop(0)
        else:
            return self.cats.pop(0)

if __name__ == '__main__':
    animal_queue = Animals()
    animal_queue.enqueue("Cat1",'Cat')
    animal_queue.enqueue("Cat2",'Cat')
    animal_queue.enqueue("Dog1",'Dog')
    animal_queue.enqueue("Cat3",'Cat')
    animal_queue.enqueue("Dog2",'Dog')
    animal_queue.enqueue("Dog3",'Dog')

    print(animal_queue.cats,animal_queue.dogs,sep="\n")

    animal_queue.dequeueany()
    print(animal_queue.cats,animal_queue.dogs,sep="\n")

    animal_queue.dequeuedog()
    print(animal_queue.cats,animal_queue.dogs,sep="\n")
