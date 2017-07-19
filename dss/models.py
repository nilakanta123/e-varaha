from __future__ import unicode_literals

from django.db import models

class Viral(models.Model):
    system_affected = models.TextField(db_column='System_affected', blank=True, null=True)
    organ_affected = models.TextField(db_column='Organ_affected', blank=True, null=True) 
    age_group = models.TextField(db_column='Age_group', blank=True, null=True)
    disease_condition = models.TextField(db_column='Disease_condition', blank=True, null=True)
    disease_row = models.TextField(db_column='Disease_row', blank=True, null=True) 
    type_of_organisms = models.TextField(db_column='Type_of_organisms', blank=True, null=True)
    causative_agent = models.TextField(db_column='Causative_agent', blank=True, null=True)
    am_findings = models.TextField(db_column='AM_findings', blank=True, null=True)
    pm_findings = models.TextField(db_column='PM_findings', blank=True, null=True)
    am_decision = models.TextField(db_column='AM_Decision', blank=True, null=True)
    am = models.TextField(db_column='AM', blank=True, null=True)
    pm_judgement = models.TextField(db_column='PM_Judgement', blank=True, null=True)
    pm = models.TextField(db_column='PM', blank=True, null=True)

    class Meta:
        db_table = 'viral'

    def __str__(self):
      return str(self.id)

class Bacterial(models.Model):
    system_affected = models.TextField(db_column='System_affected', blank=True, null=True)
    organ_affected = models.TextField(db_column='Organ_affected', blank=True, null=True) 
    age_group = models.TextField(db_column='Age_group', blank=True, null=True)
    disease_condition = models.TextField(db_column='Disease_condition', blank=True, null=True)
    disease_row = models.TextField(db_column='Disease_row', blank=True, null=True)  
    type_of_organisms = models.TextField(db_column='Type_of_organisms', blank=True, null=True)
    causative_agent = models.TextField(db_column='Causative_agent', blank=True, null=True)
    am_findings = models.TextField(db_column='AM_findings', blank=True, null=True)
    pm_findings = models.TextField(db_column='PM_findings', blank=True, null=True)
    am_decision = models.TextField(db_column='AM_Decision', blank=True, null=True)
    am = models.TextField(db_column='AM', blank=True, null=True)
    pm_judgement = models.TextField(db_column='PM_Judgement', blank=True, null=True)
    pm = models.TextField(db_column='PM', blank=True, null=True)

    class Meta:
        db_table = 'bacterial'

    def __str__(self):
      return str(self.id)

class NonInfectious(models.Model):
    system_affected = models.TextField(db_column='System_affected', blank=True, null=True)
    organ_affected = models.TextField(db_column='Organ_affected', blank=True, null=True) 
    age_group = models.TextField(db_column='Age_group', blank=True, null=True)
    disease_condition = models.TextField(db_column='Disease_condition', blank=True, null=True)
    disease_row = models.TextField(db_column='Disease_row', blank=True, null=True)  
    type_of_organisms = models.TextField(db_column='Type_of_organisms', blank=True, null=True)
    causative_agent = models.TextField(db_column='Causative_agent', blank=True, null=True)
    am_findings = models.TextField(db_column='AM_findings', blank=True, null=True)
    pm_findings = models.TextField(db_column='PM_findings', blank=True, null=True)
    am_decision = models.TextField(db_column='AM_Decision', blank=True, null=True)
    am = models.TextField(db_column='AM', blank=True, null=True)
    pm_judgement = models.TextField(db_column='PM_Judgement', blank=True, null=True)
    pm = models.TextField(db_column='PM', blank=True, null=True)

    class Meta:
        db_table = 'noninfectious'

    def __str__(self):
      return str(self.id)


class Genetic(models.Model):
    system_affected = models.TextField(db_column='System_affected', blank=True, null=True)
    organ_affected = models.TextField(db_column='Organ_affected', blank=True, null=True) 
    age_group = models.TextField(db_column='Age_group', blank=True, null=True)
    disease_condition = models.TextField(db_column='Disease_condition', blank=True, null=True)
    disease_row = models.TextField(db_column='Disease_row', blank=True, null=True)  
    type_of_organisms = models.TextField(db_column='Type_of_organisms', blank=True, null=True)
    causative_agent = models.TextField(db_column='Causative_agent', blank=True, null=True)
    am_findings = models.TextField(db_column='AM_findings', blank=True, null=True)
    pm_findings = models.TextField(db_column='PM_findings', blank=True, null=True)
    am_decision = models.TextField(db_column='AM_Decision', blank=True, null=True)
    am = models.TextField(db_column='AM', blank=True, null=True)
    pm_judgement = models.TextField(db_column='PM_Judgement', blank=True, null=True)
    pm = models.TextField(db_column='PM', blank=True, null=True)

    class Meta:
        db_table = 'genetic'

    def __str__(self):
      return str(self.id)

class Parasitic(models.Model):
    system_affected = models.TextField(db_column='System_affected', blank=True, null=True)
    organ_affected = models.TextField(db_column='Organ_affected', blank=True, null=True) 
    age_group = models.TextField(db_column='Age_group', blank=True, null=True)
    disease_condition = models.TextField(db_column='Disease_condition', blank=True, null=True)
    disease_row = models.TextField(db_column='Disease_row', blank=True, null=True)  
    type_of_organisms = models.TextField(db_column='Type_of_organisms', blank=True, null=True)
    causative_agent = models.TextField(db_column='Causative_agent', blank=True, null=True)
    am_findings = models.TextField(db_column='AM_findings', blank=True, null=True)
    pm_findings = models.TextField(db_column='PM_findings', blank=True, null=True)
    am_decision = models.TextField(db_column='AM_Decision', blank=True, null=True)
    am = models.TextField(db_column='AM', blank=True, null=True)
    pm_judgement = models.TextField(db_column='PM_Judgement', blank=True, null=True)
    pm = models.TextField(db_column='PM', blank=True, null=True)

    class Meta:
        db_table = 'parasitic'

    def __str__(self):
      return str(self.id)

class VitaminMinerals(models.Model):
    system_affected = models.TextField(db_column='System_affected', blank=True, null=True)
    organ_affected = models.TextField(db_column='Organ_affected', blank=True, null=True) 
    age_group = models.TextField(db_column='Age_group', blank=True, null=True)
    disease_condition = models.TextField(db_column='Disease_condition', blank=True, null=True)
    disease_row = models.TextField(db_column='Disease_row', blank=True, null=True) 
    type_of_organisms = models.TextField(db_column='Type_of_organisms', blank=True, null=True)
    causative_agent = models.TextField(db_column='Causative_agent', blank=True, null=True)
    am_findings = models.TextField(db_column='AM_findings', blank=True, null=True)
    pm_findings = models.TextField(db_column='PM_findings', blank=True, null=True)
    am_decision = models.TextField(db_column='AM_Decision', blank=True, null=True)
    am = models.TextField(db_column='AM', blank=True, null=True)
    pm_judgement = models.TextField(db_column='PM_Judgement', blank=True, null=True)
    pm = models.TextField(db_column='PM', blank=True, null=True)

    class Meta:
        db_table = 'vitaminminerals'

    def __str__(self):
      return str(self.id)

