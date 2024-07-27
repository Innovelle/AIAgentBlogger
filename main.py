import os  # Import os for environment variable handling
from langchain_community.chat_models import ChatOpenAI
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, WebsiteSearchTool

# Set API keys for Serper and OpenAI
os.environ["SERPER_API_KEY"] = "68a3deadf4f1602d5772e898b3ba7e980856c1c2"
os.environ["OPENAI_API_KEY"] = "sk-proj-rzpJIe6baL9QgmxN7OMnT3BlbkFJMCjmiQhSmQvVdJfZQTSQ"

research_agent = Agent(
    role='Senior Research Analyst',
    goal='Gather comprehensive information on {topic}, focusing on tech news and trends. your job is to collect information from the best sources and provide the highest quality.',
    backstory="Expert in tech research, extracting valuable insights from various sources.",
    tools=[SerperDevTool(), WebsiteSearchTool()],
    llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
    verbose=True
)

# Define the review agent
review_agent = Agent(
    role='Content Reviewer',
    goal='Analyze and synthesize information into key points and insightful reviews regarding the {topic}.',
    backstory="Skilled in critical analysis, with a knack for impactful information.",
    tools=[WebsiteSearchTool()],
    llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
    verbose=True
)

# Define the editing agent
editing_agent = Agent(
    role='Content Editor',
    goal='Edit and finalize content, ensuring readability, structure, and engagement. You will have an inquisitive style and leave questions to readers that engage their minds.',
    backstory="Experienced editor with a background in tech journalism, skilled in creating engaging and cohesive narratives.",
    tools=[WebsiteSearchTool()],
    llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
    verbose=True
)

# Define the tasks
research_task = Task(
    description="Collect comprehensive information on {topic}, focusing on tech news and trends. Use broad web searches and specific tech sites.",
    expected_output="A detailed report summarizing key findings from various sources.",
    agent=research_agent
)

review_task = Task(
    description="Analyze the gathered information and summarize key points and insights, with a broad view on the industry.",
    expected_output="An insightful review highlighting key trends and findings in tech.",
    agent=review_agent
)

editing_task = Task(
    description="Edit and finalize the article, ensuring readability, structure, and engagement. Include a compelling title, SEO keywords, and a clear introduction, body,conclusion, and meta description",
    expected_output="A polished, engaging article ready for publication with a strong title and SEO focus.",
    agent=editing_agent,
    output_file="blog_post.txt"  # Save the output to a text file
)

# Define the crew
blogging_crew = Crew(
    agents=[research_agent, review_agent, editing_agent],
    tasks=[research_task, review_task, editing_task],
    verbose=True
)

# Kickoff the crew process
result = blogging_crew.kickoff(inputs={'topic': 'Make.com Vs Cassidy Automations'})

# Debug: Print available attributes and methods of CrewOutput
print(dir(result))  # This will print all the available attributes and methods of the result object

# Extract the output from the CrewOutput object
# Since the exact method or attribute to access the data is not specified, you may need to explore the available options
# For example, if there is an attribute like 'output' or method 'get_output_data', use it accordingly
output = result.output if hasattr(result, 'output') else str(result)

# Save the result to a text file
with open("final_blog_post.txt", "w") as file:
    file.write(output)

print("Blog post created: final_blog_post.txt")