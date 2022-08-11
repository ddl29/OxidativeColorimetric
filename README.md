# Oxidative Colorimetric Analysis 🥑🍌
Measured oxidative process (enzymatic browning) on avocado and banana by taking time-lapse photographs to create line charts drawn from pixel-grid colorimetric analysis using Python. Also tried using various antioxidants to see how would it stop the oxidation.

# Context 🧬🧑‍🔬
Excited to share my first programming project completely made on my own! It was back then when I was a Biotechnology student as part of my Biochemestry research project. The challenge was come up with a creative way of measure the oxidation of fruits apart from the well-known pH analysis method. After thinking about it, I proposed my team to measure it like we would do by eye: by measuring the darkening of the surface of fruits. So that way we could take a qualitative characteristic which represents the oxidation process very faithfully and convert the data into quantitative information.

# Experiment 🔬🥑🍌
So we set up our experiment installation, by placing a time-lapsed programmed camera which would take a picture every 5 minutes. The fruits chosen were avocado and banana, and we placed them sliced over a plate on a air condition room with a constant humidity. We repeated this experiment three times.

![Control1_foto1](https://user-images.githubusercontent.com/78662124/184171093-cac0e498-4867-47f3-9096-356272c0ce36.jpg)
Link to timelapse: https://drive.google.com/file/d/1PJM0kwjZfQ83-1lUTfmWkZ-s-tZ1RrBi/view?usp=sharing

# Colorimetric analysis in Python 🐍💻
After finishing the rounds of experiments, we had tons of photographs. Since a few months before then I had taken the Introduction to Programming in Python, I thought I could solve our problem by reading in all photograph files and analyze them in how their average color was changing.

Since the fruits all had a irregular shape and the fidelity of the color might be compromised around the borders of due to shades, I only consider a mid/center grid of pixels to obtain an average single RGB color per frame. So I read every frame picture file and calculated the average and add it to an array.

Then, and since I had previously done the very common Iris flowers determination project, I take the first RGB average as our baseline (when the fruits present no oxidation) and then calculated the euclidean distance to every other RGB color in the time-lapse. Then, by considerin the last RGB color as when the fruits are completely oxidated, I obtained percentages which quantitavely measure the oxidative process.

# Posterior calculus 💻🐱
Then we filled spreedsheet with the results, performed posterior calculus like least-squares to finally obtaine beautiful line charts showing our results. Here is just one of them.

![A-M-graph](https://user-images.githubusercontent.com/78662124/184179837-9e5ae60e-8219-4d35-8ddd-812f771a70ee.png)

# Very curious discovery 🦝💡
We found it very interesting that lemon juice was the best antioxidant of the three we used (vinegar and cranberry juice). Since the main antioxidant component of lemon is ascorbic acid, we performed one extra experiment, to compare which of the two was the winner antioxidant.

![AA-A-R-graph](https://user-images.githubusercontent.com/78662124/184178983-e8838020-43b6-43cf-b01f-0bbd764dcec6.png)

As you can see, lemon juice was the outstanding antioxidant winner. Our grandmas were right. 👵👵👵
