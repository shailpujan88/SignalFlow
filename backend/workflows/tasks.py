from celery import shared_task
from executions.models import Execution
from workflows.rules import evaluate_conditions

@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=5)
def run_workflow(self, execution_id):
    execution = Execution.objects.get(id=execution_id)
    execution.status = "RUNNING"
    execution.save()

    workflow = execution.workflow
    definition = workflow.definition
    payload = execution.input_data

    try:
        if not evaluate_conditions(definition["conditions"], payload):
            execution.status = "FAILED"
            execution.error = "Conditions not met"
            execution.save()
            return

        # Simulated action
        result = {"message": "Workflow executed successfully"}
        execution.output_data = result
        execution.status = "SUCCESS"
        execution.save()

    except Exception as e:
        execution.status = "FAILED"
        execution.error = str(e)
        execution.save()
        raise
