"""
Temporal Proxy
(c) Looking Glass Solutions 2007
Licensed under GPL v2
"""

## SQL COMMANDS: http://www.postgresql.org/docs/8.3/interactive/sql-commands.html
## USE PSYCO

# Importing the required modules
import os, sys, getopt, string
from pyparsing import Literal, CaselessLiteral, Word,  delimitedList, Optional, \
    Combine, Group, alphas, nums, alphanums, ParseException, Forward, oneOf, quotedString, \
    ZeroOrMore, restOfLine, Keyword, commaSeparatedList, CharsNotIn, CaselessKeyword, QuotedString, alphas8bit, \
    NotAny, ParserElement
import time

try:
    import psyco
    psyco.full()
except:
    pass

# Variables #
LIMIT,GROUP,ORDER,BY,DISTINCT,ALL,RESTRICT,CASCADE,USING,INDEX,TABLESPACE,CREATE,DROP,TABLE,SELECT,INSERT,UPDATE,DELETE,WHERE,AS,SET,FROM,ON,INTO,VALUES,ONLY = map(CaselessKeyword, "limit group order by distinct all restrict cascade using index tablespace create drop table select insert update delete where as set from on into values only".split())
DEFAULT,NULL,TRUE,FALSE = map(CaselessKeyword, "default null true false".split())
NOTNULL = CaselessKeyword("not null")
E = CaselessLiteral("E")

arithSign = Word("+-",exact=1)

major_keywords = CREATE | DROP | SELECT | INSERT | UPDATE | DELETE | WHERE | AS | SET | FROM | ON | GROUP | ORDER
realNum = Combine( Optional(arithSign) + ( Word( nums ) + "." + Optional( Word(nums) ) |
            ( "." + Word(nums) ) ) + Optional( E + Optional(arithSign) + Word(nums) ) )
intNum = Combine( Optional(arithSign) + Word( nums ) +
            Optional( E + Optional("+") + Word(nums) ) )
keywords = DEFAULT | NULL | TRUE | FALSE

comment = "--" + restOfLine

name = ~major_keywords + Word(alphanums + alphas8bit + "_")
value = realNum | intNum | quotedString | name | keywords # need to add support for alg expressions


#INSERT Statement
"""
    INSERT INTO table [ ( column [, ...] ) ]
    { DEFAULT VALUES | VALUES ( { expression | DEFAULT } [, ...] ) [, ...] | query }
    [ RETURNING * | output_expression [ AS output_name ] [, ...] ]
    """

ins_columns = Group(delimitedList( name ))
ins_values = Group(delimitedList( value ))
# define the grammar
insert_stmt = INSERT + INTO + name.setResultsName( "table" ) \
            + Optional( "(" + ins_columns.setResultsName( "columns" ) + ")") \
            + VALUES + "(" + ins_values.setResultsName( "vals" ) + ")" + ';'
insert_stmt.ignore( comment )

def insert(query):
    global insert_stmt

    try:
        start = time.time()
        ParserElement.enablePackrat()
        tokens = insert_stmt.parseString( query )
        end = time.time()
        #query = translation.insert(tokens, information_schema, server)
        print("\tPARSE\t", round((end - start), 2), "\t", round((time.time() - end), 2))
    except ParseException:
        return False
    return tokens

tokens = insert("INSERT INTO organisation (organisation_id, name, organisation_type, parent_organisation_id) VALUES ('123','Company','123 Corp','-1');")
sql = """
SELECT Trips.Request_at Day,
       round(sum(if(status != 'completed', 1, 0)) / sum(1), 2) 'Cancellation Rate'
FROM Trips
JOIN Users
  ON Trips.Client_Id = Users.Users_Id
WHERE Users.Banned = 'No'
  AND Trips.Request_at between '2013-10-01' AND '2013-10-03'
GROUP BY Trips.Request_at
"""
print(tokens.dump())