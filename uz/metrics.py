import logging
from datadog.dogstatsd import DogStatsd


logger = logging.getLogger(__name__)


class LoggingStatsd(DogStatsd):
    """
    Adding logging to emitted metrics.
    Convenient for debugging
    """

    def _report(self, metric, metric_type, value, tags, sample_rate):
        logger.debug('[statsd] %s %s: %s', metric, metric_type, value)
        super()._report(metric, metric_type, value, tags, sample_rate)


statsd = LoggingStatsd()