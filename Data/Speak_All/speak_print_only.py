from Data.Imports.global_imports import *

engine = pyttsx3.init('sapi5')

rate = engine.getProperty('rate')
engine.setProperty('rate', 160)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

test_quorta = [
    "My name is VISE. meaning is Very Intelligent System Ever. My inventor is Mr.KillerCobra. He is very crazy "
    "and Tech guy. But He is the one and only Cyber God of the World. Although the most well known dinosaurs "
    "tend to be enormous, multi-ton animals, dinosaurs actually came in a wide variety of sizes. Although "
    "birds are the smallest dinosaurs that we know of, we still have many examples outside this group of "
    "living dinosaurs that were no larger than a house cat. For example, the small dinosaurs Microraptor and "
    "Fruitadens were probably less than a metre long as adults, and weighed less than a kilogram. One possible "
    "reason people may think dinosaurs are larger than they are is because they are often “inflated” in pop "
    "culture. For example, many people know of the large, predatory Velociraptor from the Jurasic Park "
    "franchise. However, in reality Velociraptor was about the size of a dog or a turkey, not a human. Some of "
    "the biggest dinosaurs were truly enormous though. Many of the long-necked sauropod dinosaurs were bigger "
    "than any land animal today, and the only living animals that come close to them in size are whales. When "
    "you stand up straight, the bones in your legs act like support columns. Your leg bones support your "
    "weight, without your muscles needing to actively flex and expend energy. Second, bones provide a ridged "
    "framework for muscle attachment. Raise your right hand high over your head. When you do, you can feel "
    "muscles in your shoulder flexing. The bones in your shoulder girdle provide a solid anchor against which "
    "your shoulder muscles can pull, and long bones in your arm allow it to move as single stiff unit. Third, "
    "bones provide protection and can also be major components of horns and other robust weapons. For example, "
    "your skull bones form a natural helmet that protects your brain -- a delicate organ that could be "
    "seriously damaged by an impact with an unexpectedly low doorway or rogue baseball. Finally, bones store "
    "mineral reserves. Often the resources that an animal needs to grow and develop are plentiful at one time "
    "and rare at another. During times of plenty, animals may store a valuable mineral resource, "
    "such as calcium, by growing a new bone deposit or by increasing the density of already existing bone. "
    "Later, during a time when the resource is scarce, the animal may gain access to stored minerals by "
    "reabsorbing some of its bone.Dinosaurs belong to a group of animals known as vertebrates (and so do you). "
    "Vertebrates are animals that have two special kinds of skeletal adaptations: skulls and vertebrae. "
    "Vertebrae (singular: vertebra) are structures made primarily of bone and/or cartilage that surround a "
    "portion of the spinal nerve cord. Together, vertebrae interlock with each other in a series and form the "
    "vertebral column. Fish, amphibians, turtles, snakes, birds, and mammals are all examples of vertebrates. "
    "The first vertebrates were aquatic animals that evolved over 500 million years ago. Animals that lack "
    "vertebrae are called invertebrates, and include animals like insects, spiders, snails, squids, clams, "
    "jellyfish, and worms. Since the origin of animal life, there have always been many more species of "
    "invertebrates than vertebrates. However, vertebrates are more numerous when it comes to species of large "
    "animals, especially on land. This success is probably related to the vertebral column’s ability to "
    "passively support weight and to anchor enlarged muscles."]


#engine.say(test_quorta)
#engine.runAndWait()
#engine.stop()


def speak(audio):
    print('Vise: ' + audio)
    engine.say(audio)
    engine.runAndWait()
