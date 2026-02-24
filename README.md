# Blog Automation

This project automates the creation of blog posts using AI agents. The agents are designed to research, review, and edit content on various tech topics, ensuring a comprehensive and engaging output.

## Project Structure

### Agents
* **Senior Research Analyst:** Gathers comprehensive information on the given topic, focusing on tech news and trends.
* **Content Reviewer:** Analyzes and synthesizes the gathered information into key points and insightful reviews.
* **Content Editor:** Edits and finalizes the content, ensuring readability, structure, and engagement.

### Tasks
* **Research Task:** Collects comprehensive information on the given topic, using broad web searches and specific tech sites.
* **Review Task:** Analyzes the gathered information and summarizes key points and insights, with a broad view on the industry.
* **Editing Task:** Edits and finalizes the article, ensuring readability, structure, and engagement. Includes a compelling title, SEO keywords, and a clear introduction, body, and conclusion.

## Setup Instructions

**1. Clone the Repository:**
```bash
git clone [https://github.com/YOUR_USERNAME/AIAgentBlogger](https://github.com/YOUR_USERNAME/AIAgentBlogger)
cd blog-automation
2. Set Up Virtual Environment:

Bash
python -m venv env
source env/bin/activate # On Windows use env\Scripts\activate
3. Install Dependencies:

Bash
# Note: Copied from original text, usually this would be pip install -r requirements.txt
python -m venv env
source env/bin/activate # On Windows use env\Scripts\activate
4. Set API Keys:

Serper API Key: Set your Serper API key in the environment variables.

OpenAI API Key: Set your OpenAI API key in the environment variables.

5. Run the Script:

Bash
python main.py
