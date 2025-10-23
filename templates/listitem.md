{% if href.startswith("20") %}

* [**{{ title }}**]({{ href }})
  <br><span class="smaller">{{ author }}</span>
  <br><span class="smaller">*{{ source }}*</span>

{% else %}

* [**{{ title }}**]({{ href }})
  <br><span class="smaller">{{ author }} ({{ year }})</span>

{% endif %}
