{% if "-20" in href %} {# research #}

* [**{{ title }}**]({{ href }})
  <br><span class="smaller">{{ author }}</span>
  <br><span class="smaller">*{{ source }}*, {{ year }}</span>

{% else %} {# activities #}

* [**{{ title }}**]({{ href }})
  <br><span class="smaller">{{ author }} ({{ year }})</span>

{% endif %}
