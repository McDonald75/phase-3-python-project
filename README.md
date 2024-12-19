This app will have 3 models, Member, Trainer, Fitnessplan:
The app will be able to:
allow CRUD operations for Trainers
allow CRUD operations for Members
alllow CRUD operations for the Fitnessplans
allow assignment of members to trainers
allow assignment of fitnesplans to members
allow the following search reports - plans/members/trainer by name, all members under a specific trainer/fitnessplan, all trainers facilitating a specific plan

to start, navigate to app and run : 
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