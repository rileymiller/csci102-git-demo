# Git Workshop Week 1
`git` is an extremely powerful tool that is used as a form of version control during the software development lifecycle, in laymen terms--it's how software is created in the real world. During week one of the tutorial we will learn all of the basic commands of `git` that you will need in order to keep track of your code for your school projects. Specifically, in this tutorial we will be covering: 
- How to create a repository on GitHub
- How to clone a remote repository to your computer (`git clone`)
- How to create a README
- How to create a file
- How to stage a file for a commit (`git add`)
- How to create a commit using (`git commit`)
- How to push up files to the remote repository (`git push`)

## Creating a repository on GitHub
Whenever you're starting a new project whether for school or for personal use, one of the first steps you should take is creating an empty repository on your remote version control system to keep track of your code (Github in our example). Version control is an extremely powerful tool that helps teams create software quickly and keep track of their changes. For you, you could start using it right now to keep track of your school projects to start practicing `git` fundamentals or even more importantly, to keep a backup of your code if anything were to ever happen to your computer.

To create the remote repository:
- Navigate to github.com and sign into your GitHub account.
- Next to your profile in the top-right corner of the screen click the plus sign and select 'New repository'.
[insert picture]
- Type `csci102-wk11-git` in the 'Repository name' box.
- Click the 'Initialize this repository with a README' radio box. [insert picture and instruction on creating a repo]
- Click 'Create repository'

## Cloning repository
To retrieve the remote repository to our local machine we have to clone the remote repository. To do this:
- Click the green 'Clone or download' button.
- Make sure the popup modal shows 'Clone with HTTPS'.
- Copy the generated link from input box in the 'Clone with HTTPS' modal.
- Open your terminal (Git Bash on Windows, terminal on Mac or Linux)
- Navigate to the location you'd like to clone the repository. For our tutorial we'll keep it simple and work from the root directory and just paste in `git clone <copied url for HTTPS GitHub repository here>` as soon as we open our terminal.
- Navigate into the cloned repository by typing `cd csci102-wk11-git/` into the terminal.
[insert pictures for cloning repository]

## Create a README
After navigating into your repository if you list out all of the files in the current working directory using `ls` you will see that the repository contains a README file (which we initialized while creating our repository). README files can be thought of as the repository summary or like an instruction manual. In a text editor open the README file (using the File Explorer on Windows and Finder on Mac, navigate to the README file located inside `csci102-wk11-git/` and open it using Notepad, etc.). Inside the file, copy and paste the snippet below and save the file.

```
# Week 11 Git Workshop
**Author:** <insert your name>
**Section:** <insert class section>

This is a beginner level version control workshop to help learn basic git commands and processes to allow me to use version control on school and personal projects.
```

Fill in the fields that are specific to you (name, section).