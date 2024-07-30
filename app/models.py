from django.db import models
import uuid

class Account(models.Model):
    account_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'm_account'
        app_label = 'app'

    def __str__(self):
        return self.username

class SkillCategory(models.Model):
    skill_category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    skill_category_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'm_skill_category'
        app_label = 'app'

    def __str__(self):
        return self.skill_category_name

class Training(models.Model):
    training_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    training_name = models.CharField(max_length=50)
    training_detail = models.TextField(max_length=2000, null=True, blank=True)
    skill_category_id = models.ForeignKey('SkillCategory', on_delete=models.RESTRICT, null=True, blank=True)

    class Meta:
        db_table = 'm_training'
        app_label = 'app'

    def __str__(self):
        return self.training_name
    
class Role(models.Model):
    role_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'm_role'
        app_label = 'app'

    def __str__(self):
        return self.role_name
    
class Department(models.Model):
    department_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department_name = models.CharField(max_length=50)
    is_hr_admin = models.BooleanField(default=False)

    class Meta:
        db_table = 'm_department'
        app_label = 'app'

    def __str__(self):
        return self.department_name
    
class Project(models.Model):
    project_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_id = models.ForeignKey('Account', on_delete=models.RESTRICT)
    project_name = models.CharField(max_length=50)
    project_detail = models.TextField(max_length=2000, null=True, blank=True)

    class Meta:
        db_table = 't_project'
        app_label = 'app'

    def __str__(self):
        return self.project_name
    
class Assignee(models.Model):
    assign_history_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_id = models.ForeignKey('Project', on_delete=models.RESTRICT)
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    role = models.CharField(max_length=30, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 't_assignee'
        app_label = 'app'

    def __str__(self):
        return self.assignee_id

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    full_name_str = str(last_name) + ', ' + str(first_name)
    full_name_id = str(first_name)
    # if middle_name is not None, add its first letter to full_name
    if middle_name != None:
        full_name_str = full_name_str + ' ' + str(middle_name)[0] + '.'
        full_name_id = full_name_id + '.' + str(middle_name)[0]
    full_name_id = full_name_id + '.' + str(last_name)
    full_name = models.CharField(default=full_name_str, max_length=105)
    employee_id = models.CharField(primary_key=True, default=full_name_id, max_length=103, unique=True)
    # employee_num is 8-digit number
    employee_num = models.AutoField(max_length=8, unique=True, editable=False)
    email = models.EmailField(default=employee_id + '@example.com', unique=True)
    phone_num = models.CharField(max_length=15)
    hire_date = models.DateField()
    birth_date = models.DateField()
    department_id = models.ForeignKey('Department', on_delete=models.RESTRICT)
    role_id = models.ForeignKey('Role', on_delete=models.RESTRICT)
    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 't_employee'
        app_label = 'app'

    def __str__(self):
        return self.full_name_str
    
class Skill(models.Model):
    skill_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    skill_name = models.CharField(max_length=50)
    skill_detail = models.TextField(max_length=2000, null=True, blank=True)
    skill_category_id = models.ForeignKey('SkillCategory', on_delete=models.RESTRICT)

    class Meta:
        db_table = 't_skill'
        app_label = 'app'

    def __str__(self):
        return self.skill_name

class OwnedSkill(models.Model):
    owned_skill_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    skill_id = models.ForeignKey('Skill', on_delete=models.RESTRICT)
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)

    class Meta:
        db_table = 't_owned_skill'
        app_label = 'app'

    def __str__(self):
        # return skill name from Skill model
        return Skill.objects.get(skill_id=self.skill_id).skill_name
    
class TrainingHistory(models.Model):
    training_history_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    training_id = models.ForeignKey('Training', on_delete=models.RESTRICT)
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)

    class Meta:
        db_table = 't_training_history'
        app_label = 'app'

    def __str__(self):
        return self.training_history_id
    
class Resume(models.Model):
    resume_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    resume_title = models.CharField(max_length=50)
    ex_role = models.CharField(max_length=20)
    resume_detail = models.TextField(max_length=2000, null=True, blank=True)

    class Meta:
        db_table = 't_resume'
        app_label = 'app'

    def __str__(self):
        return self.resume_title
