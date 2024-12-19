import click
from sqlalchemy.orm import joinedload
from models import session, Trainer, Fitnessplan, Member

@click.group()
def cli():
    """Fitness App CLI"""
    pass

@cli.group()
def trainer():
    """Manage trainers"""
    pass

@trainer.command()
@click.option('--name', prompt=True)
@click.option('--specialization', prompt=True)
def add(name, specialization):
    """Add a new trainer"""
    new_trainer = Trainer(name=name, specialization=specialization)
    session.add(new_trainer)
    session.commit()
    click.echo(f"Trainer added: {new_trainer}")
    
 
@trainer.command()
@click.argument('trainer_id', type=int)
def delete(trainer_id):
    """Delete a trainer"""
    trainer = session.query(Trainer).get(trainer_id)
    if trainer:
        session.delete(trainer)
        session.commit()
        click.echo(f"Trainer deleted: {trainer}")
    else:
        click.echo("Trainer not found")
        
@trainer.command()
@click.argument('trainer_id', type=int)
@click.option('--name', prompt=True)
@click.option('--specialization', prompt=True)   
def update(trainer_id, name, specialization):
    """Update trainer"""
    trainer = session.query(Trainer).get(trainer_id)
    if(trainer):
        if(name):
            trainer.name = name
        if(specialization):
            trainer.specialiation = specialization
        session.commit()
        click.echo(f"Trainer {trainer.id} updated")
    else:
        click.echo("Trainer not found")
    
@trainer.command()
def list():
    """List all trainers"""
    trainers = session.query(Trainer).all()
    for trainer in trainers:
        click.echo(trainer)

@cli.group()
def member():
    """Manage members"""
    pass

@member.command()
@click.option('--name', prompt=True)
@click.option('--email', prompt=True)
def add(name, email):
    """Add a new member"""
    new_member = Member(name=name, email=email)
    session.add(new_member)
    session.commit()
    click.echo(f"Member added: {new_member}")

@member.command()
@click.argument('member_id', type=int)
def delete(member_id):
    """Delete a member"""
    member = session.query(Member).get(member_id)
    if member:
        session.delete(member)
        session.commit()
        click.echo(f"Member deleted: {member}")
    else:
        click.echo("Member not found")

@member.command()
@click.argument("member_id", type=int)
@click.option('--name', prompt=True)
@click.option('--email', prompt=True, )
def update(member_id,name, email):
    """Update a member"""
    member = session.query(Member).get(member_id)
    if(member):
        if(name):
            member.name = name
        if(email):
            member.email = email
        session.commit()
        click.echo(f"Member {member.id} was updated")
    else:
        click.echo("Member not found")
@member.command()
def list():
    """List all members"""
    members = session.query(Member).all()
    for member in members:
        click.echo(member)

@cli.group()
def fitnessplan():
    """Manage fitness plans"""
    pass

@fitnessplan.command()
@click.option('--name', prompt=True)
@click.option('--description', prompt=True)
@click.option('--duration-weeks', type=int, prompt=True)
def add(name, description, duration_weeks):
    """Add a new fitness plan"""
    new_plan = Fitnessplan(name=name, description=description, duration_weeks=duration_weeks)
    session.add(new_plan)
    session.commit()
    click.echo(f"Fitness plan added: {new_plan}")

@fitnessplan.command()
@click.argument('plan_id', type=int)
def delete(plan_id):
    """Delete a fitness plan"""
    plan = session.query(Fitnessplan).get(plan_id)
    if plan:
        session.delete(plan)
        session.commit()
        click.echo(f"Fitness plan deleted: {plan}")
    else:
        click.echo("Fitness plan not found")

@fitnessplan.command()
@click.argument('plan_id')
@click.option('--name', prompt=True)
@click.option('--description', prompt=True)
@click.option('--duration_weeks', prompt=True, type=int)
def update(plan_id, name, description, duration_weeks):
    """Update fitness plan"""
    plan = session.query(Fitnessplan).get(plan_id)
    if(plan):
        if(name):
            plan.name = name
        if(description):
            plan.description = description
        if(duration_weeks):
            plan.duration_weeks = duration_weeks
        session.commit()
        click.echo(f"Plan {plan.id} updated")
    else:
        click.echo("Fitness plan not found")
    
@fitnessplan.command()
def list():
    """List all fitness plans"""
    plans = session.query(Fitnessplan).all()
    for plan in plans:
        click.echo(plan)

@cli.group()
def assign():
    """Assign members to trainers or fitness plans"""
    pass

@assign.command()
@click.argument('member_id', type=int)
@click.argument('trainer_id', type=int)
def member_to_trainer(member_id, trainer_id):
    """Assign a member to a trainer"""
    member = session.query(Member).get(member_id)
    trainer = session.query(Trainer).get(trainer_id)
    if member and trainer:
        member.trainer = trainer
        session.commit()
        click.echo(f"Member {member.name} assigned to Trainer {trainer.name}")
    else:
        click.echo("Member or Trainer not found")

@assign.command()
@click.argument('member_id', type=int)
@click.argument('plan_id', type=int)
def member_to_Fitnessplan(member_id, plan_id):
    """Assign a member to a fitness plan"""
    member = session.query(Member).get(member_id)
    plan = session.query(Fitnessplan).get(plan_id)
    if member and plan:
        member.fitnessplan = plan
        session.commit()
        click.echo(f"Member {member.name} assigned to Fitness Plan {plan.name}")
    else:
        click.echo("Member or Fitness Plan not found")

@cli.group()
def search():
    """Search for members, trainers, or fitness plans"""
    pass

@search.command()
@click.argument('name')
def by_name(name):
    """Search for members or trainers by name"""
    members = session.query(Member).filter(Member.name.ilike(f"%{name}%")).all()
    trainers = session.query(Trainer).filter(Trainer.name.ilike(f"%{name}%")).all()
    fitnessplan = session.query(Fitnessplan).filter(Fitnessplan.name.ilike(f"%{name}%")).all()
    
    click.echo("Members found:")
    for member in members:
        click.echo(member)
    
    click.echo("\nTrainers found:")
    for trainer in trainers:
        click.echo(trainer)
    
    click.echo("\nFitnessplan found:")
    for plan in fitnessplan:
        click.echo(plan)

@search.command()
@click.argument('trainer_id', type=int)
def members_by_trainer(trainer_id):
    """List all members under a specific trainer"""
    trainer = session.query(Trainer).options(joinedload(Trainer.members)).get(trainer_id)
    if trainer:
        click.echo(f"Members under Trainer {trainer.name}:")
        for member in trainer.members:
            click.echo(member)
    else:
        click.echo("Trainer not found")

@search.command()
@click.argument('plan_id', type=int)
def members_by_Fitnessplan(plan_id):
    """List all members under a specific fitness plan"""
    plan = session.query(Fitnessplan).options(joinedload(Fitnessplan.members)).get(plan_id)
    if plan:
        click.echo(f"Members under Fitness Plan {plan.name}:")
        for member in plan.members:
            click.echo(member)
    else:
        click.echo("Fitness Plan not found")

@search.command()
@click.argument('plan_id', type=int)
def trainers_by_Fitnessplan(plan_id):
    """List all trainers facilitating a specific fitness plan"""
    plan = session.query(Fitnessplan).options(joinedload(Fitnessplan.members).joinedload(Member.trainer)).get(plan_id)
    if plan:
        trainers = set(member.trainer for member in plan.members if member.trainer)
        click.echo(f"Trainers facilitating Fitness Plan {plan.name}:")
        for trainer in trainers:
            click.echo(trainer)
    else:
        click.echo("Fitness Plan not found")

if __name__ == '__main__':
    cli()