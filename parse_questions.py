import json

from string import Template


class Question():
    def __init__(self, question_text, answer_lines, answer_letter):
        self.question_text = question_text
        self.answer_lines = answer_lines
        self.answer_letter = answer_letter
        self.correct_answers = self._get_correct_answers()

    def _get_correct_answers(self):
        """
        Get the text for the answer to the question.
        """
        for line in self.answer_lines:
            if line.startswith(self.answer_letter):
                answer_text = line[2:]
                all_choices_text = 'All of these choices are correct'
                if all_choices_text in answer_text:
                    return [line for line in self.answer_lines \
                            if all_choices_text not in line]

                return [line]

    def get_dict(self):
        """
        Get a dict with the Question data.
        """
        return {
            'question_text': self.question_text,
            'answer_lines': self.answer_lines,
            'answer_letter': self.answer_letter,
            'correct_answers': self.correct_answers
        }


class QuestionParser():
    def __init__(self, text):
        self.text = text

    def parse(self):
        """
        Parse the raw question text into a Question object.
        """
        lines = self.text.splitlines()
        lines = [line.strip() for line in lines if line.strip()]

        assert lines[0].startswith('T'), "Line: '%s' does not start with T" % lines[0]
        answer_paren_pos = lines[0].find('(')
        answer_letter = lines[0][answer_paren_pos+1]
        return Question(lines[1], lines[2:], answer_letter)


class QuestionsParser():
    def get_question_texts(self):
        """
        Get a list of the raw text for each question.
        """
        text = self._get_text()
        texts = text.split('~~')
        return [t.strip() for t in texts if t.strip()]

    def get_questions(self):
        """
        Parse the questions and return a list of Question objects.
        """
        return [QuestionParser(t).parse() for t in self.get_question_texts()]

    def _get_text(self):
        """
        Get the raw question pool text so we can parse the questions.
        """
        with open('questions_parse.txt', 'rb') as questions_file:
            text = questions_file.read()
            text = text.decode('windows-1252')
            return text


class QuestionsMarkdownSlides():
    def __init__(self, questions):
        self.questions = questions

    def _get_markdown(self):
        """
        Get the markdown output for all of the slides.
        """
        template = self._get_slide_template()
        slide_md = ''
        for question in self.questions:
            answer_text = '<br>'.join([a[2:] for a in question.correct_answers])
            slide_md += template.substitute(question=question.question_text,
                    answer=answer_text)
        return slide_md

    def write_slides(self):
        """
        Write the markdown slides output to a file.
        """
        with open('hamslides.md', 'w') as slides_file:
            slides_file.write(self._get_markdown())

    def _get_slide_template(self):
        """
        Get the markdown template to help generate the output markdown.
        """
        with open('question_slide.tpl') as tpl_file:
            return Template(tpl_file.read())


class QuestionsJsonOutput():
    def __init__(self, questions):
        self.questions = questions

    def write(self):
        """
        Write the question data to a JSON file.
        """
        with open('questions.json', 'w') as json_file:
            obj = [q.get_dict() for q in self.questions]
            json_file.write(json.dumps(obj, indent=4, separators=(',', ': ')))


def run():
    parser = QuestionsParser()
    questions = parser.get_questions()
    slides_helper = QuestionsMarkdownSlides(questions)
    slides_helper.write_slides()

    json_helper = QuestionsJsonOutput(questions)
    json_helper.write()

run()
