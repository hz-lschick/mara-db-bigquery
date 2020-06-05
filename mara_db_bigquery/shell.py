from mara_db.shell import query_command, copy_to_stdout_command, copy_from_stdin_command, copy_command
from mara_db_bigquery import dbs

@query_command.register(dbs.BigQueryDB)
def __(db: dbs.BigQueryDB, timezone: str = None, echo_queries: bool = None):
    assert all(v is None for v in [timezone, echo_queries]), "unimplemented parameter for BigQueryDB"

    return ('bq query --use_legacy_sql=False'
            +(f' --location={db.location}' if db.location else '')
            +(f' --project_id={db.project}' if db.project else '')
            +(f' --dataset_id={db.dataset}' if db.dataset else '')
            )


@copy_to_stdout_command.register(dbs.BigQueryDB)
def __(db: dbs.BigQueryDB, header: bool = None, footer: bool = None, delimiter_char: str = None, csv_format: bool = None):
    assert all(v is None for v in [footer, delimiter_char]), "unimplemented parameter for BigQueryDB"

    if csv_format == None or csv_format == False:
        raise Exception(f'Function copy_to_stdout_command only supports CSV exports for BigQueryDB; csv_format must be set to True')

    if header == None or header == False:
        raise Exception(f'Function copy_to_stdout_command does not support headerless CSV from BigQueryDB')

    raise query_command(db) + ' --format=csv'


@copy_from_stdin_command.register(dbs.BigQueryDB)
def __(db: dbs.BigQueryDB, target_table: str, csv_format: bool = None, skip_header: bool = None,
       delimiter_char: str = None, quote_char: str = None, null_value_string: str = None, timezone: str = None):
    raise NotImplementedError(f'Function copy_to_stdout_command is not implemented for "{db.__class__.__name__}"')
