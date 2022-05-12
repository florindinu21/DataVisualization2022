library(tidyverse)
library(plotly)

plot <- plot_ly(
  df[df[, "stroke"]==1, ], x = ~bmi, y = ~avg_glucose_level, z = ~age, 
  color = ~Residence_type, colors = c('#BF382A', '#0C4B8E')

) %>%
  add_markers() %>%
  layout(
    scene = list(xaxis = list(title = 'Body mass index'),
                 yaxis = list(title = 'Avg_glucose_level'),
                 zaxis = list(title = 'Age'))
  )

plot

