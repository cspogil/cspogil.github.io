# {{ title }}

{% if author %}
**Author{{ "s" if ", " in author else "" }}:** {{ author }}
{% endif %}

{% if source %}
**Source:** {{ source }}
{% endif %}

{% if url %}
**URL:** {{ url }}
{% endif %}

{% if file %}
**File:** [{{ file }}]({{ file }})
{% endif %}
