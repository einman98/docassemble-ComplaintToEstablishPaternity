import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.ComplaintToEstablishPaternity',
      version='1.0',
      description=('Complaint to Establish Paternity'),
      long_description='# docassemble.ComplaintToEstablishPaternity\r\n\r\n## FINAL PROJECT BIOGRAPHY - Complaint to Establish Paternity\r\n\r\n## Author\r\n\r\nElicia M. Inman\r\n\r\n## Framing\r\n\r\nWhen an unmarried parent wants to file a case involving a minor child in Family Court, the first step will always be to establish paternity. Establishing paternity is important for the Court to recognize a legal relationship between a father and his child. Once this relationship is recognized, the child will be entitled to certain rights, benefits, and opportunities. Failure to establish paternity could result in time consuming litigation because the mother is only entitled custody of the child. Despite the importance of establishing paternity, several unmarried parents often overlook this step because they are simply unaware. Hence the reasoning behind my decision to automate the Complaint to Establish Paternity form. I wanted to bring this form to the forefront and streamline the process of filing any case involving a minor child. In doing so, I hope to increase access to legal practice for all people, regardless of formal education, and not just a specific type of persons. Therefore, the main potential stakeholders for my interview are any individuals seeking to establish parentage for a child born out of wedlock, as well as the Department for Children and Families, Department of Revenue, and an agency listed under G.L.c. § 28.\r\n\r\n## Research\r\n\r\nThe online legal market offers an extensive amount of information when it comes to filing for any family related matter. Any user can search on Google and research the first steps in pursuing any legal matter in court. Not to mention the individuals who can afford a lawyer and immediately be exposed to this type of information for a better understanding of the process. However, my experience in using these websites revealed a signficant problem in this model. My research consisted of asking potential users to find answers to family law questions. Afterwards, I noted some users had to sort through so much information that they lost sight of the objective. It was also brought to my attention that many users wanted to give up almost immediately. For these reasons, I found that overloading the user with more information than necessary undermines the very purpose behind increasing legal access. The problem with bombarding the user with too much information is that it leaves the users feeling overwhelmed, confused, and incompetent. Instead, the legal information that we provide online should be much more straightforward and written in plain language to bridge this gap. My experience talking to potential users was an integral part in my decision to create a simple, all-in-one, interview in the first place.\r\n\r\n## Ideation and Prototyping\r\n\r\nOnce my issue was identified, I drafted a word document with sample interview questions. My goal was to ask enough questions that filled out the form completely without exhausting the user. Then I proceeded to design a simple flowchart for my own visualization of how I wanted to control the interview flow. After my flowchart was finalized, I started to explore the idea of using QnA markup because I felt most comfortable using this tool in class. However, my first draft on QnA did not meet my expectations because the user interface was overly simplified for what I was looking to do. Therefore, I decided to create a guided online interview through the DocAssemble platform. Despite minor obstacles, I felt that this tool was the most effective because it automated a form that was stored all in the Family Law category for users to find exactly what they are looking for. My process in starting this project began on Adobe Acrobat Professional and Google Doc. I found that it was best to use Adobe because Documate was creating many issues for me. I also found Google Doc to be extremely useful in maintaining a list of variables that I can use for future collaborative projects.\r\n\r\n## User Testing\r\n\r\nAfter I had a somewhat solid foundation on the DocAssemble platform, I was able to start engaging in a round of user testing. I had about 10 students in the Family Advocacy Clinic run the interview themselves to see if their outcomes were accurate. I targeted these users specifically because their experience using family law websites would provide valuable insight on how I can conduct my interview in a way that encourages the user to fill out the form themself without feeling overwhelmed. Each of the 10 users were capable of completing the guided interview with their own scenarios in mind and without an error message. However, my supervisor had pointed out two questions in my interview that needed to be reworded for better understanding. From here, I went back to work in the Playground and implemented the changes from the user feedback to address the concerns that were raised. Finally, I was able to reach a set of questions that I was comfortable with and finalized my guided interview for review. In conclusion, the user testing was extremely useful because it ensured me that all potential users can access this form. \r\n\r\n## Refinement\r\n\r\nAs I mentioned in the User Testing section, I used the feedback from potential users to refine my guided interview in the Playground. After my interview was updated, I returned to the clinic to ask for opinions from the past users. Their feedback indicated that the users preferred the straightforward and plain language structure of my updated interview. In addition to their feedback, I spent time going through the questions myself to ensure it was completed to my own satisfication. I would also like to note that the signature block was intentionally left blank for users to wet sign. It is also worth noting that no users had a strong preference over whether their signature was included or not. Two users however, brought up how e-Filing may create another obstacle for the older or less experienced user. Regardless, the signature block of the form is properly labeled in the PDF and the code still includes the formatting for a signature in case the signature block is required. \r\n\r\n## Complexity and Robustness\r\n\r\nGiven that this form was merely a list of questions to checkbox, using an expert system, machine learning algorithm, or data scraping from a data source did not seem necessary. However, I was able to make use of my document automation skills for the purposes of completing this form. However, I found that Documate was not functioning properly so I had to switch gears and learn how to use Adobe Acrobate Pro to finish filling in the variables. This part was the only part that I was completely lost on but it was not too complicated. Fortunately, I feel as though I was able to achieve my goals with the tools we learned from class.\r\n\r\n## Impact and Efficiencies\r\n\r\nWith the help of this guided interview, any user looking to file a case involving a minor child will find it to be much more productive than sorting through several resources on Google. The money saved from time consuming litigation will help individuals tremendously. Litigation is already a lengthy and expensive process so any users looking to save will find my guided interview to be exactly what they are looking for. Furthermore, any user can explore my guided interview to better understand what the Court is looking for in this specific matters. It is clear that this form will not only increase levels of encouragement and exposure, but also impact the way users litigate their own cases.\r\n\r\n## Fitness and Completion\r\n\r\nIt is my position that an automated guided interview to establish paternity is much more efficient than the status quo. Currently, users who are looking to file for any case involving a child must sort through so much information to begin the process. Not to mention, the lack of confidence will leave users feeling uncertain if they are answering the right questions and filling out the correct form. This form will such a positive impact because the questions are designed to appear when it only applies to you. This leaves no room for confusion and users are able to confidently file a form because they will know the proper information has been filled out.\r\n\r\n## Real World Viability\r\n\r\nMy opinion is that my interview is close to being ready for real-world use. Aside from the signature block that I had mentioned earlier, the rest of the form operates to full completion. It is my hope that I will have some time in the foreseeable future to refine this interview and include it in the bigger project that I am working on in the Legal Innovations and Technology Lab. Otherwise, this interview is accessible to be tested. \r\n\r\n## Sustainability\r\n\r\nOther than the signature block, I do not anticipate any significant updates to be made on this form. It is my hope to set up the signature block in a way that users can have the option to e-file the form directly to the relevant and appropriate court if they so choose. If not, I have confidence in the Suffolk LIT Lab that some change could be implemented to resolve this issue. In regards to maintenance for the form, I am not entirely certain how any maintenance will be made other than through my work as a LIT Fellow and the standard maintenance that the DocAssemble server runs.\r\n',
      long_description_content_type='text/markdown',
      author='Elicia M. Inman',
      author_email='einman@suffolk.edu',
      license='The MIT License',
      url='https://courtformsonline.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['docassemble.ALMassachusetts>=0.1.2', 'docassemble.AssemblyLine>=2.19.0', 'docassemble.MassAccess>=0.3.0'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/ComplaintToEstablishPaternity/', package='docassemble.ComplaintToEstablishPaternity'),
     )

