from cron_explainer.parser import parse


class CronJob:

    def __init__(self, expression: str):
        self._expression = expression
        self._parse()
    
    def _parse(self):
        unit_expressions = self._expression.split(' ')
        attributes = ['minute', 'hour', 'day', 'month', 'day_week', 'command']

        if len(unit_expressions) != 6:
            raise ValueError('Cron expression is not valid.')

        for attribute, unit_expression in zip(attributes, unit_expressions):
            data = unit_expression

            if attribute != 'command':
                data = parse(unit_expression, attribute)

            setattr(self, attribute, data)
