import jmespath

def parse_homework(data):
            subjects_ids = jmespath.search("subjects[*].id", data)
            homework = {}
            for i in subjects_ids:
                homework[i] = {
                    "name": ' '.join(jmespath.search(f"subjects[?id==`{i}`].name", data)),
                    "task": '; '.join(jmespath.search(f"works[?subjectId==`{i}`].text", data))
                }
            text = ""
            for i in homework.values():
                text += f"{i['name']}: {i['task']} \n\n"
            return text