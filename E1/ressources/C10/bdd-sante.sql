#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------

#------------------------------------------------------------
# Table: Reponse questionnaire
#------------------------------------------------------------

CREATE TABLE heroku_0060548401e7c15.Reponse_questionnaire(
        id_reponse Int  Auto_increment  NOT NULL ,
        reponse    Varchar (50) NOT NULL
	,CONSTRAINT Reponse_questionnaire_PK PRIMARY KEY (id_reponse)
)ENGINE=InnoDB;

#------------------------------------------------------------
# Table: Questionnaire
#------------------------------------------------------------

CREATE TABLE heroku_0060548401e7c15.Questionnaire(
        id_questionnaire          Int  Auto_increment  NOT NULL ,
        Age                       Int NOT NULL ,
        Gender                    Varchar (50) NOT NULL ,
        self_employed             Varchar (50) NOT NULL ,
        family_history            Varchar (50) NOT NULL ,
        work_interfere            Varchar (50) NOT NULL ,
        no_employees              Varchar (50) NOT NULL ,
        remote_work               Varchar (50) NOT NULL ,
        tech_company              Varchar (50) NOT NULL ,
        benefits                  Varchar (50) NOT NULL ,
        care_options              Varchar (50) NOT NULL ,
        wellness_program          Varchar (50) NOT NULL ,
        seek_help                 Varchar (50) NOT NULL ,
        anonymity                 Varchar (50) NOT NULL ,
        `leave`                     Varchar (50) NOT NULL ,
        mental_health_consequence Varchar (50) NOT NULL ,
        phys_health_consequence   Varchar (50) NOT NULL ,
        coworkers                 Varchar (50) NOT NULL ,
        supervisor                Varchar (50) NOT NULL ,
        mental_health_interview   Varchar (50) NOT NULL ,
        phys_health_interview     Varchar (50) NOT NULL ,
        mental_vs_physical        Varchar (50) NOT NULL ,
        obs_consequence           Varchar (50) NOT NULL ,
        id_reponse                Int NOT NULL
	,CONSTRAINT Questionnaire_PK PRIMARY KEY (id_questionnaire)

	,CONSTRAINT Questionnaire_Reponse_questionnaire_FK FOREIGN KEY (id_reponse) REFERENCES Reponse_questionnaire(id_reponse)
)ENGINE=InnoDB;

INSERT INTO Reponse_questionnaire VALUES (1, "Besoin d'un traitement");
INSERT INTO Reponse_questionnaire VALUES (2, "Pas besoin d'un traitement")


