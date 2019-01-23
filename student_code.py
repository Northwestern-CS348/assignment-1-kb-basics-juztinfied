import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        self.facts.append(fact)

        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """


        print("Asserting {!r}".format(fact))
        
    def kb_ask(self, fact):
        q = fact
        q_statement = fact.statement
        response = ListOfBindings()
        
        if (not is_var(q_statement.terms[0]) and not is_var(q_statement.terms[1])):
            for f in self.facts:
                if (match(q_statement, f.statement)):
                    newbindings = match(q_statement, f.statement)
                    response.add_bindings(newbindings, f)

            if response.__len__() == 0:
                return False
            
            else:
                return response
        
        elif (not is_var(q_statement.terms[0]) and is_var(q_statement.terms[1])):# if question is like color bigbox ?y
            for f in self.facts:
                if q_statement.predicate == f.statement.predicate and q_statement.terms[0].__eq__(f.statement.terms[0]):
                    newbindings = match(q_statement, f.statement)
                    response.add_bindings(newbindings, f)

            if response.__len__() == 0:
                return False 
            
            else:
                return response
        
        elif  (is_var(q_statement.terms[0]) and not is_var(q_statement.terms[1])):
            for f in self.facts:
                if q_statement.predicate == f.statement.predicate and q_statement.terms[1].__eq__(f.statement.terms[1]):
                    newbindings = match(q_statement, f.statement)
                    response.add_bindings(newbindings, f)

            if response.__len__() == 0:
                return False 
            
            else:
                return response


        elif  (is_var(q_statement.terms[0]) and is_var(q_statement.terms[1])):
            for f in self.facts:
                if q_statement.predicate == f.statement.predicate:
                    newbindings = match(q_statement, f.statement)
                    response.add_bindings(newbindings, f)

            if response.__len__() == 0:
                return False 
            
            else:
                return response

        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
