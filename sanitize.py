from contextlib import closing
import psycopg2
import argparse
import logging

_logger = logging.getLogger(__name__)
parser = argparse.ArgumentParser(description="Sanitize production database")
parser.add_argument('database')
parser.add_argument('--env')
args = parser.parse_args()

def sanitize(cr, args, database):
    
    _logger.info('TEST')
    cr.execute("""update res_partner SET email = ''""")
    
    cr.execute("""update ir_mail_server SET active = false""")
    
    cr.execute("""update ir_cron SET active = false""")
    return


with closing(psycopg2.connect("dbname=" + args.database)) as conn:
    with closing(conn.cursor()) as cr:
        sanitize(cr, args, args.database)
    
    conn.commit()
    