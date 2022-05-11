


ggplot(df, aes(x = bmi, y = age)) +
   geom_point(color = "chocolate4") +
  labs(x = "BMI", y = "Age") +  scale_x_discrete(breaks = round(seq(0, 70, by = 5),0))+ggtitle("Body mass index by age")+
  theme(axis.title = element_text(color = "sienna", size = 15, face = "bold"),
   axis.title.y = element_text(face = "bold.italic"),plot.title = element_text(lineheight = 8, size = 16))+theme_light()

  