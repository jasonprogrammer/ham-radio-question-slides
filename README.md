# Ham Radio Slides

The goal of this project is to create web slides for each of the possible questions that could appear on the Ham Radio Technician test. Once the basic set of slides is created, the Markdown slides can be hand-modified to add additional links, images, and other helpful content.

## Are the slides online?

[Yes, they're available here](https://jasonprogrammer.github.io/hamslides/tech-questions.html).

## What are the steps involved in creating the slides?

1. Parse a somewhat hand-modified version of the [Ham Radio Technician question pool](http://ncvec.org/downloads/2014-2018%20Tech%20Pool.txt).
2. Create a Markdown file that [Cleaver](https://github.com/jdan/cleaver) can read and turn into slides.

## Can I modify the slides for my own use?

Absolutely! Just grab the markdown file (`dist/hamslides.md`) and use [Cleaver](https://github.com/jdan/cleaver) to create your slides.

## Can I get a simple JSON file with the questions?

There is a JSON file in this repo (`dist/questions.json`) containing some of the question data. Feel free to use it to generate other slides! I created the parser pretty quickly, so no guarantees that everything is perfect.

The [HamStudy.org](https://hamstudy.org/) support team has a much better (more detailed) set of JSON files with the questions. Feel free to email them for details.

## What is the purpose of each file in the repo?

`build.sh` - Commands used to parse the input file (`questions_parse.txt`) and build the markdown (`hamslides.md`) slides.  
`parse_questions.py` - Python code used to parse the questions file.  
`questions_parse.txt` - Hand-modified version of the `questions.txt` file (easier to parse).  
`questions.txt` - Unmodified 2014-2018 question pool text file.  
`question_slide.tpl` - A template file to help create each Markdown slide section.

## Did you just sloppily hack this Python code together?

Yes, I needed to get the slides done quickly.

## License

MIT
