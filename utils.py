




Skills=[]
Contribs_Index=[]
Projects_Index=[]

Contribs=[]
Projects=[]





# contrib=Contrib(contrib_index=contrib_index,skills_dict=skills_dict)
class Contrib:
    def __init__(self,contrib_index,skills_dict) -> None:

        self.contrib_index=contrib_index
        self.contrib_name=Contribs_Index[contrib_index]


        self.skill_orig=skills_dict

        self.skills=skills_dict

        self.project=None

        self.wait=False

        self.working_skill=None

        self.reset()

    def reset(self):
        self.project=None

        self.wait=False

        self.working_skill=None

        self.skills=self.skill_orig.copy()



    def increase_skill(self):


        # for skill, level in self.project.skills.items():
        #     print()

        # skill_index=self.working_skill[0]
        # skill_level=self.working_skill[1]

        # current_skill_level=self.skills[skill_index]

        # # print(current_skill_level)

        # if skill_level > current_skill_level:
        #     current_skill_level+=1

        # print(current_skill_level)

            

        


        # print()

        
        # self.skills[]+=1


        return True

    def assign_project(self,project,skill):
        global Projects

        if not self.wait:

            if not self.project:
                self.project=project
                self.working_skill=skill

                return True

            


            if self.project == project:
                return True

        return False

    
    def project_completed(self,project):
        
        # if not self.project:
        #     return False 

        if self.project == project:


            self.increase_skill()
            self.project=None
            self.wait=True




        


    # def isbusy(self):



        # for project_skill in self.project.skills:
        #     print(project_skill)





#  project=Project(project_index=project_index,skills_dict=skills_dict,duration=duration,score=score,best_before=best_before)
      
class Project:
    def __init__(self,project_index,skills_dict,skills_list,duration,score,best_before) -> None:


        self.project_index=project_index
        self.project_name=Projects_Index[project_index]
        self.skills=skills_dict
        self.skills_list=skills_list

        # print(skills_list)

        #in days
        self.duration =duration

        self.score=score

        #in days from start of simulation
        self.best_before=best_before

        self.contribs=[]

        


        self.total_time=0

        self.time_passed=0

        self.started=False

        self.done=False

        self.reset()

    

    def reset(self):

        self.total_time=0

        self.time_passed=0

        self.started=False

        self.done=False



    


    def get_score(self):

        
        # print(f'{self.project_name} {self.total_time} {self.best_before} {self.score} {self.time_passed} {self.duration}')

        



        if self.total_time <=  self.best_before:
            return self.score
        else:

            diff = self.total_time - self.best_before

            score= self.score - diff

            if score < 0:
                score =0

            return score




    def complete_project(self):
        
        self.done=True

        for contrib in self.contribs:
            contrib.project_completed(self)






    def assign_contribs(self,project_contribs):
        # print(project_contribs)

        self.contribs=project_contribs




    def start_project(self):


        contribs_free=True


        for i, contrib in enumerate(self.contribs):

            skill_index=self.skills_list[i]

            skill=(skill_index,self.skills[skill_index])

            if not contrib.assign_project(self,skill):
                contribs_free=False



                
            

            # print(contrib.contrib_name)

        if contribs_free:
            self.started=True
            return True
        else:
            return False




    def running(self):

        if not self.done:
        
            self.total_time+=1
            

            if not self.started:
                self.start_project()


            if self.started:
                self.time_passed+=1

            
                if  self.time_passed == self.duration:

                    self.complete_project()

                    return True




            
            
            return False





def read_input(file_name_in):


    Lines=[]

    global Skills
    global Contribs_Index
    global Projects_Index

    global Contribs
    global Projects

    with open(file_name_in, "r") as f:
        Lines = f.readlines()


    first_line=Lines[0].split()
    num_contribs=int(first_line[0])
    num_projects=int(first_line[1])


    # contrib_count=0
    # project_count=0

    i=1



    
    for _ in range(num_contribs):

        contrib_line=Lines[i].split()
        contrib_name=contrib_line[0]

        if contrib_name not in Contribs_Index:
            Contribs_Index.append(contrib_name)
        contrib_index=Contribs_Index.index(contrib_name)


        num_skills=int(contrib_line[1])
        i+=1

        skills_dict={}

        for _ in range(num_skills):

            skill_line=Lines[i].split()



            skill_name=skill_line[0]
            skill_level=int(skill_line[1])

            if skill_name not in Skills:
                Skills.append(skill_name)

            skill_index=Skills.index(skill_name)

            # print(skill_index)
            # skill_obj=(skill_index,skill_level)
            # skills_list.append(skill_obj)
            skills_dict[skill_index]=skill_level

            i+=1


        contrib=Contrib(contrib_index=contrib_index,skills_dict=skills_dict)
        Contribs.append(contrib)

        # print(skills_dict)
        

    for _ in range(num_projects):

        project_line=Lines[i].split()

        project_name=project_line[0]
        duration=int(project_line[1])
        score=int(project_line[2])
        best_before=int(project_line[3])
        num_skills=int(project_line[4])


        if project_name not in Projects_Index:
            Projects_Index.append(project_name)

        project_index=Projects_Index.index(project_name)

        # print(project_line)

        i+=1

        skills_dict={}
        skills_list=[]


        for _ in range(num_skills):

            skill_line=Lines[i].split()



            skill_name=skill_line[0]
            skill_level=int(skill_line[1])

            if skill_name not in Skills:
                Skills.append(skill_name)

            skill_index=Skills.index(skill_name)

            # print(skill_index)

            # skill_obj=(skill_index,skill_level)
            # skills_list.append(skill_obj)

            skills_dict[skill_index]=skill_level
            skills_list.append(skill_index)


            i+=1

        # print(skills_dict)

        project=Project(project_index=project_index,skills_dict=skills_dict,duration=duration,score=score,best_before=best_before,skills_list=skills_list)
        Projects.append(project)


        
    # print(Skills)
    # print(Projects)
    # print(Contribs)







planned_projects=[]


def read_output(file_name_out):


    Lines=[]

    global Skills
    global Contribs_Index
    global Projects_Index

    global Contribs
    global Projects

    global planned_projects

    with open(file_name_out, "r") as f:
        Lines = f.readlines()


    first_line=Lines[0].split()
    num_project_planned=int(first_line[0])
    # print(num_project_planned)

    i = 1

    for _ in range(num_project_planned):

        project_line=Lines[i].split()

        project_name=project_line[0]

        # if project_name not in Projects_Index:
        #     Projects_Index.append(project_name)

        project_index=Projects_Index.index(project_name)
        
        i+=1

        project_contribs_line=Lines[i].split()

        contrib_indexs=[]

        for project_contrib_name in project_contribs_line:


            # print(project_contrib_name)

            # if contrib_name not in Contribs_Index:
            #     Contribs_Index.append(contrib_name)

            contrib_index=Contribs_Index.index(project_contrib_name)
            contrib_indexs.append(contrib_index)

        

        planned_project=(project_index,contrib_indexs)

        planned_projects.append(planned_project)

        i+=1
    
    # print(planned_projects)









def simulate():


    global Projects
    global Contribs

    global planned_projects

    running_projects=[]

    for planned_project in planned_projects:
        # print(planned_project)
        project_index=planned_project[0]
        project_contribs_line=planned_project[1]



        
        project_contribs=[Contribs[contrib_index] for contrib_index in project_contribs_line]

        running_projects.append(project_index)

        Projects[project_index].assign_contribs(project_contribs)

    

    num_running_projects=len(running_projects)

    running=True

    done=0

    
    while(running):


        for contrib in Contribs:
            contrib.wait=False


        for project_index in running_projects:
            
            if Projects[project_index]:
                if Projects[project_index].running():
                    done+=1
                    project_index=None

        if done>=num_running_projects:
            break





def calculate_score():

    global Projects

    total_score=0

    for project_dict in planned_projects:

        project_index=project_dict[0]

        project=Projects[project_index]

        # print(f'{project.done}')

        score=project.get_score()

        # print(score)

        total_score+=score

    return total_score





        



    # second_line=Lines[1].split()
    # third_line=Lines[2].split()

    # print(Lines)


def reset():

    for project in Projects:

        project.reset()

    for contrib in Contribs:

        contrib.reset()

        

def save_output(file_name_out):

    # print(planned_projects)
    
    with open(file_name_out,"w") as f:
    # L = ["This is Delhi \n","This is Paris \n","This is London"] 


        num_planned_projects=f'{len(planned_projects)}\n'
        f.write(num_planned_projects)
        # print(num_planned_projects)


        for project in planned_projects:
            project_name=Projects_Index[project[0]]
            contribs=project[1]
            output=f'{project_name}\n'
            f.write(output)
            project_contribs=[Contribs_Index[contrib] for contrib in contribs]
            # print(output)

            project_contribss=" ".join(project_contribs)
            # print(project_contribss)
            f.write(f'{project_contribss}\n')






def brute_force():

    # print(len(Projects))
    # print(len(Contribs))
    

    for project in Projects:

        project_contribs=[]

        for skill_index, level in project.skills.items():

            for contrib in Contribs:

                contrib_skill_level=contrib.skills.get(skill_index)

                if contrib_skill_level:
                    if contrib_skill_level >= level:

                        # print()
                        project_contribs.append(contrib.contrib_index)
                        break



        planned_projects.append((project.project_index,project_contribs))


    print(planned_projects)
        
                    

