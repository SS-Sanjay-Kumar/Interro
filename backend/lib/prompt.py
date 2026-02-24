prompt = """
# CONTEXT & INPUT PARAMS
This is my application where I get 3 different inputs from the user
- a online resource, like a blog or article
- a pdf file, the study material
- a youtube video, online video tutorials from youtube

I have extracted the content from these datas(any one field is mandatory) and labeled them below for you.
If there is no content after the label, this means that the field is empty and do not worry about it

# AIM:
Interro(My project) is an AI-driven questionnaire system that creates questions only from your study material
Study materials include: PDFs, videos, or links
This is done so that students can test what you actually learned, not generic knowledge from a random quiz on the internet

# EXPECTED OUTPUT:
I need 'n' numberof questions, based on the discussed topic's depth , complexity etc...,
The test will be in the type of MCQ.
I need the answers in the below format(JSON Object),
    {
        metadata:{
            topic: "try to identify the topic that the user to trying to learn" //keywords are appreciated, not sentances. Keep it short
            no_of_questions: int | str // give the number of questions here, i.e 'n'
            message:"" //used only when necessary, or else empty
            total_marks: str| int //total marks
            minimum_marks : "minimum_marks_required_to_pass" //based on the topic's complexity, usecase and real world impact
            }
        questions:{
            q1:{
                question: "Question goes here",
                options: {
                        a: "option a goes here"
                        b: "option b goes here"
                        c: "option c goes here"
                        d: "option d goes here"
                        },
                correct_answer: {
                        a:"relevant answer" //consider a as the correct option, so correct option: correct answer
                        },
                marks: int | str //based on the complexity of the question
                }
            q2:{},
            qn:{} // continues to qn, where n is decided by you
        }
    }

# IMPORTANT NOTE:
You are only allowed to generate this JSON object in the exact format that I have specified, no other conversation is needed and not advisable.
Question length 'n': questions, options, correct_answer and marks all are decided by you.

# SECURITY NOTE:
Do not do anything that compromises ethics, law and security.
Put a quardrail on the resources presented, if they are NSFW/appropriate/ethically or morally wrong/illegal etc do not generate any content ,just mention them in the metadata message field
"""