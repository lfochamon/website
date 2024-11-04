Title: Publications
Date: 1002-01-01

<style>
.pubs_list ul{
  padding: 0 30px;
  font-size: 17px;
  list-style-type: none;
}

.pubs_list li{
  margin: 0 0 15px 0;
}

/* Style the button that is used to open and close the collapsible content */
.collapsible a {
  cursor: pointer;
}

.active {
  font-weight: bold;
}

.collapsible p {
  margin: 0;
}

/* Style the collapsible content. Note: hidden by default */
.collapsible-content {
  display: none;
  overflow: hidden;
  margin-top: 1rem;
}
</style>


{% macro collapsible_bibtex(pub) -%}
<span class="collapsible">
[&nbsp;<a class="collapsible_link">Bibtex</a>&nbsp;]
<div class="collapsible-content">
<pre>{{ pub.bibtex }}</pre>
</div>
</span>
{%- endmacro %}


{% set pub_dict = [('Preprints', 'preprint'), ('Patents', 'patent'), ('Journals', 'journal'), ('ML and systems conferences', 'conf_ml'), ('Control conferences', 'conf_control'), ('Signal processing conferences', 'conf_sp'), ('Technical reports', 'other')] %}

# Publications [[Google Scholar](https://scholar.google.ca/citations?user=FIm-l-sAAAAJ&hl=en)]

{% for name, tag in pub_dict %}
- [{{name}}](#{{tag}})
{% endfor %}

&nbsp;

-----

## Selected publications

<div class="pubs_list">
<ul>
  {% for publication in publications | sort(True, attribute='year') | selectattr('key', 'in', ['Chamon24c', 'Calvo-Fullana24s', 'Chamon23c', 'Robey21a', 'Chamon20p', 'Chamon20ta', 'Kalogerias20b', 'Eisen19l', 'Paternain19c']) %}
  <li id='{{ publication.key }}'>
    {{ publication.text }}
    {%- if publication.award -%}
      &nbsp;<strong>({{ publication.award }})</strong>
    {%- endif %}
    <br />
    {% for label, target, event in [('PDF', publication.pdf, 'Publications'), ('arXiv', publication.arxiv, 'Publications'), ('YouTube', publication.video, 'Presentations'), ('Slides', publication.slides, 'Presentations'), ('Poster', publication.poster, 'Presentations'), ('Link', publication.url, 'Publications')] -%}
      {{- "[&nbsp;<a href=\"%s\" onClick=\"gtag('event', '%s', {'event_category' : '%s', 'event_label' : '%s'});\">%s</a>&nbsp;]" % (target, event, label, publication.key, label) if target -}}
    {%- endfor -%}
    {{ collapsible_bibtex(publication) }}
  {% endfor -%}
</ul>
</div>

-----

&nbsp;

{% for name, tag in pub_dict %}
<h2 id="{{ tag }}">{{ name }}</h2>

<div class="pubs_list">
<ul>
  {% for publication in publications_lists[tag] | sort(True, attribute='year') %}
    <li id='{{ publication.key }}'>
      {{ publication.text }}
      {% if publication.award %}
        <strong>({{ publication.award }})</strong>
      {% endif %}
    <br />
    {% for label, target in [('PDF', publication.pdf), ('arXiv', publication.arxiv), ('YouTube', publication.video), ('Slides', publication.slides), ('Poster', publication.poster), ('Link', publication.url)] -%}
      {{- "[&nbsp;<a href=\"%s\" onClick=\"gtag('event', 'Publications', {'event_category' : '%s', 'event_label' : '%s'});\">%s</a>&nbsp;]" % (target, label, publication.key, label) if target -}}
    {%- endfor -%}
    {{ collapsible_bibtex(publication) }}
    </li>
  {% endfor -%}
</ul>
</div>

&nbsp;

{% endfor %}



<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].getElementsByClassName("collapsible_link")[0].addEventListener("click", function() {
    this.classList.toggle("active");

    // Sentinel
    var content = this.nextElementSibling;
    while (content) {
      if (content.matches('.collapsible-content')) break;
      content = sibling.nextElementSibling;
    }

    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
</script>
