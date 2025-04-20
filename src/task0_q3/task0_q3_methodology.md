My approach was to just write a publisher that publishes String of the Command, then in the Subscriber code, defining a class for position, and defining its variables and methods accordingly. \
I realized later that the data had to be communicated using a custom message, so I just changed the class code accordingly and made a message. \
\
The code moves the bot by 5units in whatever direction is commanded, or turns the bot as commanded. \
By opening 2 terminals and commanding in the terminal running publisher, we can see the position of the bot in the terminal running subscriber. \
\
I ran into a lot of problems with message generation in the terminal, but after working it all out in CMakeLists.txt, package.xml and restarting Ubuntu, it all worked out.
