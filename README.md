# Ham Radio Slides

The goal of this project is to create web slides for each of the possible questions that could appear on the Ham Radio Technician test.

## What are the steps involved in creating the slides?

1. Parse a somewhat hand-modified version of the [Ham Radio Technician question pool](http://ncvec.org/downloads/2014-2018%20Tech%20Pool.txt).
2. Create a Markdown file that [Cleaver](https://github.com/jdan/cleaver) can read and turn into slides.

## Are the slides online?

[Yes, they're available here](https://jasonprogrammer.github.io/hamslides/).

## Can I modify the slides for my own use?

Absolutely! Just grab the markdown file (`hamslides.md`) and use [Cleaver](https://github.com/jdan/cleaver) to create your slides.

## Can I get a simple JSON file with the questions?

There is a JSON file in this repo (`dist/questions.json`) containing some of the question data. Feel free to use it to generate other slides! I created the parser pretty quickly, so no guarantees that everything is perfect.

## License

MIT
