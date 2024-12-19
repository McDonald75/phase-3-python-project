This app will have 3 models, Member, Trainer, Fitnessplan:
The app will be able to:
allow CRUD operations for Trainers
allow CRUD operations for Members
alllow CRUD operations for the Fitnessplans
allow assignment of members to trainers
allow assignment of fitnesplans to members
allow the following search reports - plans/members/trainer by name, all members under a specific trainer/fitnessplan, all trainers facilitating a specific plan

To start, navigate to app and run (in env shell): 
python cli.py --help

expected output
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

  Fitness App CLI

Options:
  --help  Show this message and exit.

Commands:
  assign       Assign members to trainers or fitness plans
  fitnessplan  Manage fitness plans
  member       Manage members
  search       Search for members, trainers, or fitness plans
  trainer      Manage trainers

With each command, you can run --help to show usage, e.g
python cli.py assign --help

NOTE : 
To run these commands, please navigate into the app folder, to access the cli.py file